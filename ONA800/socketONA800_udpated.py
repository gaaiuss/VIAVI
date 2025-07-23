import socket
import csv
from pathlib import Path
from datetime import datetime
import time


# Cria diretório de resultados
thisDir = Path(__name__).resolve().parent
resultsDir = thisDir / "resultados"

if not resultsDir.exists():
    resultsDir.mkdir(exist_ok=True)

# Substituir pelo IP do ONA-800
host = "10.55.8.156"
# host = "192.168.0.207"

# A porta é sempre 5600
port = 5600

# Definição dos testes a serem realizados
# cf é a frequencia central da banda a ser testada


testes = [testChannelPower, testOccupiedBW,
          testSpectrumEmissionMask, testACLR, testSubframe]

testesDict = {"Channel Power": testChannelPower,
              "Occupied BW": testOccupiedBW,
              "Spectrum Emission Mask": testSpectrumEmissionMask,
              "ACLR": testACLR,
              "Subframe": testSubframe}

# testesDict = {"Subframe": testSubframe}

parametrosDict = {"Channel Power": ["Channel Power", "P/F", "Spectral Density", "PTA Ratio"],
                  "Occupied BW": ["Occupied BW", "P/F", "Integrated Power", "Occupied Power"],
                  "Spectrum Emission Mask": ["Lower1 Peak Power", "Lower1 P/F",
                                             "Upper1 Peak Power", "Upper1 P/F",
                                             "Lower2 Peak Power", "Lower2 P/F",
                                             "Upper2 Peak Power", "Upper2 P/F",
                                             "Lower3 Peak Power", "Lower3 P/F",
                                             "Upper3 Peak Power", "Upper3 P/F"
                                             ],
                  "ACLR": ["Reference Power", "Lower1 Relative Power", "Lower1 P/F",
                           "Lower1 Absolute Power", "Upper1 Relative Power", "Upper1 P/F",
                           "Upper1 Absolute Power", "Lower2 Relative Power", "Lower2 P/F",
                           "Lower2 Absolute Power", "Upper2 Relative Power", "Upper2 P/F",
                           "Upper2 Absolute Power"
                           ],
                  "Subframe": ["Subframe Power", "EVM P-SS", "EVM S-SS", "EVM PBCH", "EVM PCFICH",
                               "EVM PHICH", "EVM PDCCH", "EVM RS", "EVM DATA 16QAM", "EVM DATA 64QAM",
                               "EVM DATA 26QAM", "Power P-SS", "Power S-SS", "Power PBCH", "Power PCFICH",
                               "Power PHICH", "Power PDCCH", "Power RS", "Power DATA 16QAM",
                               "Power DATA 64QAM", "Power DATA 26QAM", "Reg/RB 64QAM", "OFDM Symbol Power",
                               "Freq. Error Hz", "Freq. Error ppm", "Freq. Error P/F", "Time Error",
                               "Data EVM RMS", "Data EVM RMS %", "Data EVM Peak", "Data EVM Peak %",
                               "Data EVM Peak Symbol", "RS EVM RMS", "RS EVM RMS %", "RS EVM Peak",
                               "RS EVM Peak %", "RS EVM Symbol"
                               ]
                  }


# Lista de frequencias a serem testadas
# centerFrequency = [1812.6, 1870, 2135, 2160]
centerFrequency = [1812.6, 1842.5, 1870, 2160]

# Rotina que monta o script de cada teste para cada frequencia central


def create_test(cf, testName):
    try:
        message = eval(f"f'''{testName}'''")
        return message
    except Exception as e:
        return f"Error processing the template: {e}"


# Gera nome do arquivo de testes
def nomeArquivo():
    ano = datetime.now().year
    mes = datetime.now().month
    dia = datetime.now().day
    hora = datetime.now().hour
    minuto = datetime.now().minute
    fileName = f"{ano}-{mes}-{dia}-{hora}-{minuto}.txt"
    return fileName


resultsFile = resultsDir / nomeArquivo()

# Rotina que estabelece a conexão com o ONA-800
# e envia o batch de comandos.
# A espera de 12s é necessária para o equipamento
# alternar os modos de teste
# Não tentei encontrar o valor mínimo de espera....


def setup_inicial(host=host, port=5600, comando=setup_parameters):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    s.sendall(comando.encode("utf-8"))
    s.shutdown(socket.SHUT_WR)
    time.sleep(10)

    return


def netcat(host, port=5600, comando="*IDN?"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))

    s.sendall(comando.encode("ascii"))
    time.sleep(12)
    data = s.recv(4096)

    # Encerra a conexão
    s.shutdown(socket.SHUT_WR)

    return data.decode("UTF-8").split()


def escreveArquivo(teste, cf, resultadoParcial):
    parametros = parametrosDict[teste]
    tempDict = {k: v for k, v in zip(parametros, resultadoParcial)}

    if resultsFile.exists():
        with open(resultsFile, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for key, value in tempDict.items():
                writer.writerow([key, cf, value])
    else:
        with open(resultsFile, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for key, value in tempDict.items():
                writer.writerow([key, cf, value])


startTime = time.monotonic()
setup_inicial()

for teste in testesDict:
    for cf in centerFrequency:
        print(f"Testing {teste} for {cf} MHz")
        test = create_test(cf, testesDict[teste])
        resultadoParcial = netcat(host, port, test)
        escreveArquivo(teste, cf, resultadoParcial)

print(f"Total execution time: {time.monotonic() - startTime:.2f} seconds")
