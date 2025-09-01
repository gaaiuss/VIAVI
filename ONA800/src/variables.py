import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

# Directories
ROOT_DIR = Path(__file__).parent.parent
OUTPUT_DIR = ROOT_DIR / "output"
Path.mkdir(OUTPUT_DIR, exist_ok=True)  # Make output dir if it not exists

# Result file
_now = datetime.now()
_file_name = _now.strftime("%Y-%m-%d-%H-%M.txt")
OUTPUT_FILE = OUTPUT_DIR / _file_name

# HOST
load_dotenv()
HOST = os.getenv('HOST')  # ONA-800 IP

# Port
PORT = 5600

# Lista de frequencias a serem testadas
# CENTER_FREQUENCY = [1812.6, 1870, 2135, 2160]
CENTER_FREQUENCY = [1812.6, 1842.5, 1870, 2160]

# Definição dos testes a serem realizados
# cf é a frequencia central da banda a ser testada
SETUP_PARAMETERS = """SYSTem:LAUNch
LTE:FDD:MODE signalAnalyzerLTEFDD
LTE:FDD:AMPlitude:PREAmp:FIRSt Off
LTE:FDD:AMPlitude:ATTenuation:VALUE 30
LTE:FDD:AMPLitude:EXTernal 44
LTE:FDD:ANTenna:SELect Auto
"""

_testChannelPower = """
    LTE:FDD:MODE channelPower
    LTE:FDD:FREQuency:CENTer {cf} MHz
    LTE:FDD:CHANnel:POWer?
    LTE:FDD:CHANnel:POWer:JUDGE?
    LTE:FDD:CHANnel:POWer:SPECtral:DENSity?
    LTE:FDD:CHANnel:POWer:PTA:RATio?
"""

_testOccupiedBW = """
    LTE:FDD:MODE occupiedBW
    LTE:FDD:FREQuency:CENTer {cf} MHz
    LTE:FDD:OCCupied:BW?
    LTE:FDD:OCCupied:BW:JUDGE?
    LTE:FDD:OCCupied:BW:INTegrated:POWer?
    LTE:FDD:OCCupied:BW:OCCupied:POWer?
"""

_testSpectrumEmissionMask = """
    LTE:FDD:MODE spectrumEmissionMask
    LTE:FDD:FREQuency:CENTer {cf} MHz
    LTE:FDD:SEM:PEAK:LOWER1:POWER?
    LTE:FDD:SEM:PEAK:LOWER1:JUDGe?
    LTE:FDD:SEM:PEAK:UPPER1:POWER?
    LTE:FDD:SEM:PEAK:UPPER1:JUDGe?
    LTE:FDD:SEM:PEAK:LOWER2:POWER?
    LTE:FDD:SEM:PEAK:LOWER2:JUDGe?
    LTE:FDD:SEM:PEAK:UPPER2:POWER?
    LTE:FDD:SEM:PEAK:UPPER2:JUDGe?
    LTE:FDD:SEM:PEAK:LOWER3:POWER?
    LTE:FDD:SEM:PEAK:LOWER3:JUDGe?
    LTE:FDD:SEM:PEAK:UPPER3:POWER?
    LTE:FDD:SEM:PEAK:UPPER3:JUDGe?
"""

_testACLR = """
    LTE:FDD:MODE adjacentChannelPower
    LTE:FDD:FREQuency:CENTer {cf} MHz
    LTE:FDD:ACP:REFERENCE:POWer?
    LTE:FDD:ACP:INTegration:LOWer01:RELATIVE:POWer?
    LTE:FDD:ACP:INTegration:LOWER01:JUDGe?
    LTE:FDD:ACP:INTegration:LOWer01:ABSolute:POWer?
    LTE:FDD:ACP:INTegration:UPPER01:RELATIVE:POWer?
    LTE:FDD:ACP:INTegration:UPPer01:JUDGe?
    LTE:FDD:ACP:INTegration:UPPER01:ABSolute:POWer?
    LTE:FDD:ACP:INTegration:LOWer02:RELATIVE:POWer?
    LTE:FDD:ACP:INTegration:LOWER02:JUDGe?
    LTE:FDD:ACP:INTegration:LOWer02:ABSolute:POWer?
    LTE:FDD:ACP:INTegration:UPPER02:RELATIVE:POWer?
    LTE:FDD:ACP:INTegration:UPPer02:JUDGe?
    LTE:FDD:ACP:INTegration:UPPER02:ABSolute:POWer?
"""

_testSubframe = """
    LTE:FDD:MODE subframe
    LTE:FDD:FREQuency:CENTer {cf} MHz
    LTE:FDD:SUBFrame:POWer?
    LTE:FDD:SUBFrame:EVM:PSS?
    LTE:FDD:SUBFrame:EVM:SSS?
    LTE:FDD:SUBFrame:EVM:PB?
    LTE:FDD:SUBFrame:EVM:PCFI?
    LTE:FDD:SUBFrame:EVM:PHI?
    LTE:FDD:SUBFrame:EVM:PDC?
    LTE:FDD:SUBFrame:EVM:RS?
    LTE:FDD:SUBFrame:EVM:QAM16?
    LTE:FDD:SUBFrame:EVM:QAM64?
    LTE:FDD:SUBFrame:EVM:QAM256?
    LTE:FDD:SUBFrame:POWer:PSS?
    LTE:FDD:SUBFrame:POWer:SSS?
    LTE:FDD:SUBFrame:POWer:PB?
    LTE:FDD:SUBFrame:POWer:PCFI?
    LTE:FDD:SUBFrame:POWer:PHI?
    LTE:FDD:SUBFrame:POWer:PDC?
    LTE:FDD:SUBFrame:POWer:RS?
    LTE:FDD:SUBFrame:POWER:QAM16?
    LTE:FDD:SUBFrame:POWER:QAM64?
    LTE:FDD:SUBFrame:POWER:QAM256?
    LTE:FDD:SUBFrame:REGard:RB:QAM64?
    LTE:FDD:SUBFrame:OFDM:SYMBol:POWer?
    LTE:FDD:SUBFrame:FREQuency:ERRor:HZ?
    LTE:FDD:SUBFrame:FREQuency:ERRor:PPM?
    LTE:FDD:SUBFrame:FREQuency:ERRor:JUDGE?
    LTE:FDD:SUBFrame:TIME:ERRor?
    LTE:FDD:SUBFrame:DATA:EVM:RMS:NORMal?
    LTE:FDD:SUBFrame:DATA:EVM:RMS:ACCumulate?
    LTE:FDD:SUBFrame:DATA:EVM:PEAK:NORMAL?
    LTE:FDD:SUBFrame:DATA:EVM:PEAK:ACCumulate?
    LTE:FDD:SUBFrame:DATA:EVM:PEAK:SYMBol?
    LTE:FDD:SUBFrame:RS:EVM:RMS:NORMAL?
    LTE:FDD:SUBFrame:RS:EVM:RMS:ACCUMULATE?
    LTE:FDD:SUBFrame:RS:EVM:PEAK:NORMAL?
    LTE:FDD:SUBFrame:RS:EVM:PEAK:ACCUMULATE?
    LTE:FDD:SUBFrame:RS:EVM:PEAK:SYMBOL?
    """

TESTS = {"Channel Power": _testChannelPower,
         "Occupied BW": _testOccupiedBW,
         "Spectrum Emission Mask": _testSpectrumEmissionMask,
         "ACLR": _testACLR,
         "Subframe": _testSubframe}

PARAMETERS = {
    "Channel Power": [
        "Channel Power", "P/F", "Spectral Density", "PTA Ratio"
    ],
    "Occupied BW": [
        "Occupied BW", "P/F", "Integrated Power", "Occupied Power"
    ],
    "Spectrum Emission Mask": [
        "Lower1 Peak Power", "Lower1 P/F",
        "Upper1 Peak Power", "Upper1 P/F",
        "Lower2 Peak Power", "Lower2 P/F",
        "Upper2 Peak Power", "Upper2 P/F",
        "Lower3 Peak Power", "Lower3 P/F",
        "Upper3 Peak Power", "Upper3 P/F"
    ],
    "ACLR": [
        "Reference Power", "Lower1 Relative Power", "Lower1 P/F",
        "Lower1 Absolute Power", "Upper1 Relative Power", "Upper1 P/F",
        "Upper1 Absolute Power", "Lower2 Relative Power", "Lower2 P/F",
        "Lower2 Absolute Power", "Upper2 Relative Power", "Upper2 P/F",
        "Upper2 Absolute Power"
    ],
    "Subframe": [
        "Subframe Power", "EVM P-SS", "EVM S-SS", "EVM PBCH", "EVM PCFICH",
        "EVM PHICH", "EVM PDCCH", "EVM RS", "EVM DATA 16QAM", "EVM DATA 64QAM",
        "EVM DATA 26QAM", "Power P-SS", "Power S-SS", "Power PBCH",
        "Power PCFICH", "Power PHICH", "Power PDCCH", "Power RS",
        "Power DATA 16QAM", "Power DATA 64QAM", "Power DATA 26QAM",
        "Reg/RB 64QAM", "OFDM Symbol Power", "Freq. Error Hz",
        "Freq. Error ppm", "Freq. Error P/F", "Time Error", "Data EVM RMS",
        "Data EVM RMS %", "Data EVM Peak", "Data EVM Peak %",
        "Data EVM Peak Symbol", "RS EVM RMS", "RS EVM RMS %", "RS EVM Peak",
        "RS EVM Peak %", "RS EVM Symbol"
    ]
}
