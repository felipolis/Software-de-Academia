def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um numero inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[Usuario preferiu não digitar esse numero.\033[m")
            return 0
        else:
            return n