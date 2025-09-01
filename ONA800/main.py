import csv
import socket
import time
from time import sleep

from src.variables import (CENTER_FREQUENCY, HOST, OUTPUT_FILE, PARAMETERS,
                           PORT, SETUP_PARAMETERS, TESTS)


# Rotina que monta o script de cada teste para cada frequencia central
# Rotina que estabelece a conexão com o ONA-800
# e envia o batch de comandos.
# A espera de 12s é necessária para o equipamento
# alternar os modos de teste
# Não tentei encontrar o valor mínimo de espera....
def evaluate_test(testName) -> str:
    try:
        message = eval(f"f'''{testName}'''")
        return message
    except Exception as e:
        return f"Error processing the template: {e}"


def initial_setup():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(SETUP_PARAMETERS.encode("utf-8"))
    s.shutdown(socket.SHUT_WR)
    sleep(10)


def netcat(command="*IDN?") -> list[str]:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(command.encode("ascii"))
    sleep(12)
    data = s.recv(4096)
    s.shutdown(socket.SHUT_WR)  # Close connection
    return data.decode("UTF-8").split()


def write_csv(test: str, cf: float, partial_result: list[str]):
    parameters = PARAMETERS[test]
    temp_dict = {k: v for k, v in zip(parameters, partial_result)}
    if OUTPUT_FILE.exists():
        with open(OUTPUT_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for key, value in temp_dict.items():
                writer.writerow([key, cf, value])
    else:
        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for key, value in temp_dict.items():
                writer.writerow([key, cf, value])


if __name__ == '__main__':
    startTime = time.monotonic()
    initial_setup()
    for test_type in TESTS:
        for cf in CENTER_FREQUENCY:
            print(f"Testing {test_type} for {cf} MHz")
            evaluated_test = evaluate_test(TESTS[test_type])
            partial_result = netcat(evaluated_test)
            write_csv(test_type, cf, partial_result)
    print(
        f"\nTotal execution time: {time.monotonic() - startTime:.2f} seconds")
