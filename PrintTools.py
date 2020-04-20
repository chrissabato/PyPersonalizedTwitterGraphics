# Print single line in box
# ═══════════════════════════════════════════ 
def PrintBox(content,width=0):
    if width == 0:
        width = len(content)+2
    print("╔".ljust(width+1,"═") +"╗")
    print("║ "+content.ljust(width-1)+ "║")
    print("╚".ljust(width+1,"═") +"╝")

# Print Menu Box
# ═══════════════════════════════════════════ 
def menu():
    print("╔════════════════════════════════════════╗")
    print("║ Select an Option                       ║")
    print("╠════════════════════════════════════════╣")
    print("║ 1 — Read tweet replies                 ║")
    print("║ 2 — Generate images                    ║")
    print("║ 3 — Send images                        ║")
    print("║ 4 — Edit Setting                       ║")
    print("║ 5 — Exit                               ║")
    print("╚════════════════════════════════════════╝")

    userinput = input()
    return userinput

# Print Settings
# ═══════════════════════════════════════════ 
def PrintSetting(setting,config):
    print("╔═══════╦════════════════════════════════╗")
    print("║   KEY ║ "+ setting.ljust(31) + "║")
    print("╠═══════╬════════════════════════════════╣")
    print("║ VALUE ║ "+ config[setting].ljust(31) + "║")
    print("╚═══════╩════════════════════════════════╝")
    
    newSetting = input()
    return newSetting
