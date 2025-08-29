import csv
import os
import socket
import time
from time import sleep

from dotenv import load_dotenv

from src.path_variables import RESULT_FILE
from src.test_variables import (CENTER_FREQUENCY, PARAMETERS, PORT,
                                SETUP_PARAMETERS, TESTS)

load_dotenv()
HOST = os.getenv('HOST')  # ONA-800 IP


# Rotina que monta o script de cada teste para cada frequencia central
def create_test(testName) -> str:
    try:
        message = eval(f"f'''{testName}'''")
        return message
    except Exception as e:
        return f"Error processing the template: {e}"

# Rotina que estabelece a conexão com o ONA-800
# e envia o batch de comandos.
# A espera de 12s é necessária para o equipamento
# alternar os modos de teste
# Não tentei encontrar o valor mínimo de espera....


def initial_setup():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(SETUP_PARAMETERS.encode("utf-8"))
    s.shutdown(socket.SHUT_WR)
    sleep(10)


def netcat(command="*IDN?"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(command.encode("ascii"))
    sleep(12)
    data = s.recv(4096)

    # Close connection
    s.shutdown(socket.SHUT_WR)

    return data.decode("UTF-8").split()


def write_csv(test: str, cf: float, partial_result: list[str]):
    parameters = PARAMETERS[test]
    temp_dict = {k: v for k, v in zip(parameters, partial_result)}

    if RESULT_FILE.exists():
        with open(RESULT_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for key, value in temp_dict.items():
                writer.writerow([key, cf, value])
    else:
        with open(RESULT_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for key, value in temp_dict.items():
                writer.writerow([key, cf, value])


if __name__ == '__main__':
    startTime = time.monotonic()
    initial_setup()

    for test in TESTS:
        for cf in CENTER_FREQUENCY:
            print(f"Testing {test} for {cf} MHz")
            test = create_test(TESTS[test])
            partial_result = netcat(test)
            write_csv(test, cf, partial_result)

    print(f"Total execution time: {time.monotonic() - startTime:.2f} seconds")
