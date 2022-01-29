from colorama import Fore, Style
import random

def wordle_function(wordle, input):
    wordle_list = list(wordle.upper())
    input_list = list(input.upper())
    res = {
    "isWinner": False,
    "inputWord": "",
    'colorWord': "",
    "emojiRes": ""}    
    # 1. Compruebo que están en la misma posición (intersección de listas)
    true_list = [input_list[idx] if wordle_list[idx] == input_list[idx]  else "" for idx in range(0,len(input_list))]
    false_list = [input_list[idx] if wordle_list[idx] != input_list[idx]  else "" for idx in range(0,len(input_list))]
    # 2. Compruebo que existe pero está en una posición diferente:
    wrong_position = [char if char in wordle_list else "" for char in false_list]
    not_in_wordle = [char if char not in wordle_list else "" for char in false_list]
    '''
    print("Letras que están en la posición correcta: " +str(true_list))
    print("Letras que no están en la posición correcta: " +str(wrong_position))
    print("Letras que no están en la palabra: " +str(not_in_wordle))
    '''
    # Pinta y colorea
    green_position = [idx for idx in range(0,len(true_list)) if true_list[idx] != ""]
    yellow_position = [idx for idx in range(0,len(wrong_position)) if wrong_position[idx] != ""]
    red_position = [idx for idx in range(0,len(not_in_wordle)) if not_in_wordle[idx] != ""]
    color_word = []
    emoji_res = []
    for i in range(0,len(input_list)):
        if i in green_position:
            green = f'{Fore.GREEN}{input[i]}{Style.RESET_ALL}'
            color_word.append(green)
            emoji_res.append('🟩')
        if i in yellow_position:
            yellow = f'{Fore.YELLOW}{input[i]}{Style.RESET_ALL}'
            color_word.append(yellow)
            emoji_res.append('🟨')
        if i in red_position:
            red = f'{Fore.RED}{input[i]}{Style.RESET_ALL}'
            color_word.append(red)
            emoji_res.append('🟥')
    #print(''.join(str(char) for char in color_word))
    #print(''.join(str(emoji) for emoji in emoji_res))
    if(wordle_list == input_list):
        res['isWinner'] = True
        res['inputWord'] = input.upper()
        res['emojiRes'] = emoji_res
        res['colorWord'] = ''.join(str(char) for char in color_word)
    else:
        res['isWinner'] = False
        res['inputWord'] = input.upper()
        res['emojiRes'] = emoji_res
        res['colorWord'] = ''.join(str(emoji) for emoji in color_word)
    return res

def main():
    intentos = 1
    centinela = True
    wordle = random.choice(open("final.txt").readlines())
    wordle = wordle.replace('\n','')
    dict_res = {}
    while(centinela):
        if intentos <=5:
            print(wordle)
            entrada = input("Escribe una palabra de 5 caracteres (intento: "+str(intentos)+"): ")
            while(len(entrada) != 5):
                entrada = input("Palabra de longitud distinta a 5. Escribe otra palabra: (intento "+str(intentos)+"): ")
            res = wordle_function(wordle, entrada)
            dict_res[res['colorWord']] = res['emojiRes']
            if(res['isWinner']):
                print("¡Has ganado! " +str(intentos)+"/6")
                for key in dict_res:
                    print(key + " " + ''.join(str(emoji) for emoji in dict_res[key]))
                centinela = False
            else:
                for key in dict_res:
                    print(key + " " + ''.join(str(emoji) for emoji in dict_res[key]) + " " + str(intentos) + "/6")
                intentos = intentos + 1
        if(intentos > 5):
            print("¡Has perdido!")
            print("La palabra era: "+wordle)
            for key in dict_res:
                print(key + " " + ''.join(str(emoji) for emoji in dict_res[key]) + " X/6")            
                centinela = False


def lectura_y_escritura(input):
    with open('final.txt', 'w') as w:
        with open(input,'r') as r:
            for linea in r:
                if len(linea) == 6:
                    linea = linea.upper()
                    if 'Á' in linea:
                        w.write(linea.replace('Á','A'))
                    elif 'É' in linea:
                        w.write(linea.replace('É','E'))
                    elif 'Í' in linea:
                        w.write(linea.replace('Í','I'))
                    elif 'Ó' in linea:
                        w.write(linea.replace('Ó','O'))
                    elif 'Ú' in linea:
                        w.write(linea.replace('Ú','U'))
                    else:
                        w.write(linea)
    with open("final.txt", "r") as f_in:
        unicos = set(f_in.readlines())
    with open("final.txt", "w") as f_out:
        f_out.write("".join(unicos))
                
if __name__ == "__main__":
    main()





