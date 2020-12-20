import sys

asm2bin = {
    "NOP": "00000 000 000000 00",
    "HALT": "00000 000 000000 01",
    "LDI R{:d}, #{:X}h": "00001 {:0>3} {:0>8}",
    "LD R{:d}, R{:d}": "00010 {:0>3} {:0>3} 000 00",
    "ST R{:d}, R{:d}": "00010 {:0>3} {:0>3} 000 01",
    "MV R{:d}, R{:d}": "00010 {:0>3} {:0>3} 001 00",
    "PUSH R{:d}": "00011 000 {:0>3} 000 00",
    "POP R{:d}": "00011 {:0>3} 000 000 01",
    "INC R{:d}": "00100 {:0>3} 000 000 00",
    "DEC R{:d}": "00100 {:0>3} 000 000 01",
    "NEG R{:d}": "00100 {:0>3} 000 000 10",
    "NOT R{:d}": "00100 {:0>3} 000 000 11",
    "SHL R{:d}": "00100 {:0>3} 000 001 00",
    "SHR R{:d}": "00100 {:0>3} 000 001 01",
    "ASL R{:d}": "00100 {:0>3} 000 001 10",
    "ASR R{:d}": "00100 {:0>3} 000 001 11",
    "ADD R{:d}, R{:d}, R{:d}": "00101 {:0>3} {:0>3} {:0>3} 00",
    "ADC R{:d}, R{:d}, R{:d}": "00101 {:0>3} {:0>3} {:0>3} 01",
    "SUB R{:d}, R{:d}, R{:d}": "00101 {:0>3} {:0>3} {:0>3} 10",
    "SBC R{:d}, R{:d}, R{:d}": "00101 {:0>3} {:0>3} {:0>3} 11",
    "AND R{:d}, R{:d}, R{:d}": "00110 {:0>3} {:0>3} {:0>3} 00",
    "OR R{:d}, R{:d}, R{:d}": "00110 {:0>3} {:0>3} {:0>3} 01",
    "XOR R{:d}, R{:d}, R{:d}": "00110 {:0>3} {:0>3} {:0>3} 10",
    "CMP R{:d}, R{:d}": "00111 000 {:0>3} {:0>3} 00",
    "CLC": "01000 000 000 000 00",
    "STC": "01000 000 000 000 01",
    "CLI": "01000 000 000 000 10",
    "STI": "01000 000 000 000 11",
    "BR": "10000 {:0>11}",
    "BRNZ": "10001 {:0>11}",
    "BRZ": "10010 {:0>11}",
    "BRNS": "10011 {:0>11}",
    "BRS": "10110 {:0>11}",
    "BRNC": "10101 {:0>11}",
    "BRC": "10110 {:0>11}",
    "BRNV": "10111 {:0>11}",
    "BRV": "11000 {:0>11}",
    "BRA": "11001 {:0>11}",
    "BRBE": "11010 {:0>11}",
    "BRGT": "11011 {:0>11}",
    "BRGE": "11100 {:0>11}",
    "BRLE": "11101 {:0>11}",
    "BRLT": "11110 {:0>11}",
    "CALL": "11111 {:0>11}",
    "RET": "01001 000000 000 00",
    "RETI": "01001 000000 000 01"
    }

form = "\t{:X}{:X} {:X}{:X}\t; {}\t{}"

def convertInt():
    print("")
    print("Input 'asm', 'bin' or 'q'")
    print("e.g., 'LDI R0, #20h', '00001 000 0010 0000', 'q'")
    print("")
    while(True):
        inp = input("> ")

        if(inp == "q"):
            break

        elif(inp[0] == "0" or inp[0] == "1"):
            out = inp
            outTemp = out.split(" ")
            for i in asm2bin:
                if(outTemp[0] == asm2bin[i].split(" ")[0]):
                    if(outTemp[0][0] != "1" and outTemp[0] != "00001"):
                        if(outTemp[-1] == asm2bin[i].split(" ")[-1]):
                            if(outTemp[0] == "00010"):
                                if(outTemp[-2] != asm2bin[i].split(" ")[-2]):
                                    continue
                        else:
                            continue

                    if(outTemp[0][0] == "1" and len(outTemp) == 4):
                        outTemp[1] = "".join(outTemp[1:])
                        outTemp.pop(3)
                        outTemp.pop(2)
                    elif(outTemp[0] == "00001" and len(outTemp) == 4):
                        outTemp[2] = "".join(outTemp[2:])
                        outTemp.pop(3)

                    inpTemp = i.split(" ")
                    if(outTemp[0][0] != "1"):
                        temp = asm2bin[i].split(" ")
                        inpIdx = 1
                        for j in range(1, len(temp)):
                            if("{" in temp[j]):
                                inpTemp[inpIdx] = inpTemp[inpIdx].format(int(outTemp[j], 2))
                                inpIdx += 1

                    for j in range(len(outTemp)):
                        if(len(outTemp[j]) == 11):
                            outTemp.append(outTemp[j][3:])
                            outTemp[j] = outTemp[j][:3]
                        elif(len(outTemp[j]) == 8):
                            outTemp.append(outTemp[j][4:])
                            outTemp[j] = outTemp[j][:4]
                    inp = " ".join(inpTemp)
                    out = " ".join(outTemp)
                    res = out.replace(" ", "")
                    print(form.format(int(res[8:12], 2), int(res[12:], 2), int(res[:4], 2), int(res[4:8], 2), out, inp))
                    print("")
                    break

        else:
            inpTemp = inp.split(" ")
            for i in range(1, len(inpTemp)):
                inpTemp[i] = inpTemp[i].strip(" ,hR#")

            for i in asm2bin:
                if(inpTemp[0] == i.split(" ")[0]):
                    outTemp = asm2bin[i].split(" ")
                    outTemp[0] = asm2bin[i]

            if(outTemp[0][0] == "1"):
                print("Sorry!")
                print("")
                continue

            inpIdx = 1
            for i in range(1, len(outTemp)):
                if("{" in outTemp[i]):
                    outTemp[i] = outTemp[i].format(bin(int(inpTemp[inpIdx], 0x10))[2:])
                    inpIdx += 1

            if(len(outTemp) == 1):
                out = outTemp[0]
            elif(len(outTemp) == 2):
                out = outTemp[0].format(outTemp[1])
            elif(len(outTemp) == 3):
                out = outTemp[0].format(outTemp[1], outTemp[2])
            else:
                out = outTemp[0].format(outTemp[1], outTemp[2], outTemp[3])

            outTemp[0] = outTemp[0].split(" ")[0]
            for i in range(len(outTemp)):
                if(len(outTemp[i]) == 11):
                    outTemp.append(outTemp[i][3:])
                    outTemp[i] = outTemp[i][:3]
                elif(len(outTemp[i]) == 8):
                    outTemp.append(outTemp[i][4:])
                    outTemp[i] = outTemp[i][:4]
            out = " ".join(outTemp)
            res = out.replace(" ", "")
            print(form.format(int(res[8:12], 2), int(res[12:], 2), int(res[:4], 2), int(res[4:8], 2), out, inp))
            print("")

if __name__ == "__main__":
    convertInt()
