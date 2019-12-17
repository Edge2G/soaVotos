import curses
from curses import textpad
import subprocess

def decode_auth_cliente(msg):
    auth = msg[12:-1]

    if auth == '1':
        return '1'

    if auth == '2':
        return '2'

def decode_vote_results(msg):
    msg = msg[20:]

    primera_fila = True
    vote_name = ""
    results = {}
    opcion = ""
    valor = ""

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i in range(0, len(msg)):
        #print i, " ", msg[i]
        if msg[i] == ' ' or msg[i] == '|' or msg[i] == '':
            continue
        if msg[i] == '\n':
            if primera_fila == True:
                vote_name = opcion
                primera_fila = False
                continue
            else:
                results[opcion] = valor
                opcion = ""
                valor = ""
                continue
        if msg[i] in numbers:
            valor = valor + str(msg[i])
            continue
        else:
            opcion = opcion + str(msg[i])
            continue

    results.pop(vote_name)

    return vote_name, results

def print_header(header_win, max_cols):
    header_win.addstr(1, int((max_cols/2)-25), "  _____              __      __   _            ",  curses.color_pair(1))
    header_win.addstr(2, int((max_cols/2)-25), " / ____|             \ \    / /  | |           ",  curses.color_pair(1))
    header_win.addstr(3, int((max_cols/2)-25), "| (___   ___   __ _   \ \  / /__ | |_ ___  ___ ",  curses.color_pair(1))
    header_win.addstr(4, int((max_cols/2)-25), " \___ \ / _ \ / _` |   \ \/ / _ \| __/ _ \/ __|",  curses.color_pair(1))
    header_win.addstr(5, int((max_cols/2)-25), " ____) | (_) | (_| |    \  / (_) | || (_) \__ \\",  curses.color_pair(1))
    header_win.addstr(6, int((max_cols/2)-25), "|_____/ \___/ \__,_|     \/ \___/ \__\___/|___/",  curses.color_pair(1))

def print_select_menu(stdscr, menu_selection, menu_entries):
    stdscr.clear()
    max_y, max_x = stdscr.getmaxyx()

    for i, item in enumerate(menu_entries):
        x_mid = max_x//2 - len(item)//2
        y_mid = max_y//2 + i*2

        if i == menu_selection:
            stdscr.addstr(y_mid, x_mid, item, curses.color_pair(2))
        else:
            stdscr.addstr(y_mid, x_mid, item)

    stdscr.refresh()

def authenticate_vote_menu(stdscr):
    stdscr.clear()
    max_y, max_x = stdscr.getmaxyx()
    box = [[max_y//3, max_x//3], [2*(max_y//3), 2*(max_x//3)]]
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

    title_txt = "Ingrese Credenciales"
    user_txt = "Usuario:"
    passwd_txt = "Contraseña:"
    matricula_txt = "N° de Matricula:"
    carrera_txt = "Carrera:"

    user_input = ""
    passwd_input = ""
    passwd_visible = ""
    matricula_input = ""
    carrera_input = ""

    user = "user"
    passwd = "passwd"
    matricula = "matr"
    carrera = "carr"
    
    stdscr.addstr(box[0][0]-1, (max_x//2)-(len(title_txt)//2), title_txt, curses.color_pair(2))
    stdscr.addstr(6*box[0][0]//5, box[0][1]+6, user_txt, curses.color_pair(2))
    stdscr.addstr(7*box[0][0]//5, box[0][1]+6, passwd_txt, curses.color_pair(2))
    stdscr.addstr(8*box[0][0]//5, box[0][1]+6, matricula_txt, curses.color_pair(2))
    stdscr.addstr(9*box[0][0]//5, box[0][1]+6, carrera_txt, curses.color_pair(2))

    curses.curs_set(1)
    curses.echo()
    stdscr.move(6*box[0][0]//5, box[0][1]+6+len(user_txt)+1)

    is_auth = False

    while(is_auth != True):
        # Input para campo usuario
        while True:
            key = stdscr.getch()
            if key == curses.KEY_ENTER or key in [10, 13]:
                stdscr.move(7*box[0][0]//5, box[0][1]+6+len(passwd_txt)+1)
                break

            elif key == 8 or key == 127 or key == curses.KEY_BACKSPACE:
                    user_input = user_input[:-1]
                    stdscr.addstr(6*box[0][0]//5, box[0][1]+6+len(user_txt)+1+len(user_input), "   ")
                    stdscr.move(6*box[0][0]//5, box[0][1]+6+len(user_txt)+1+len(user_input))

            else:
                if len(user_input) == 20:
                    stdscr.addstr(6*box[0][0]//5, box[0][1]+6+len(user_txt)+1+len(user_input), " ")
                    stdscr.move(6*box[0][0]//5, box[0][1]+6+len(user_txt)+1+len(user_input))
                elif len(user_input) < 20:
                    user_input = user_input + chr(key)

        # Input para campo passwd
        while True:
            key = stdscr.getch()
            if key == curses.KEY_ENTER or key in [10, 13]:
                stdscr.move(8*box[0][0]//5, box[0][1]+6+len(matricula_txt)+1)
                break

            elif key == 8 or key == 127 or key == curses.KEY_BACKSPACE:
                passwd_input = passwd_input[:-1]
                stdscr.addstr(7*box[0][0]//5, box[0][1]+6+len(passwd_txt)+1+len(passwd_input), "      ")
                stdscr.move(7*box[0][0]//5, box[0][1]+6+len(passwd_txt)+1+len(passwd_input))

            else:
                if len(passwd_input) == 20:
                    stdscr.addstr(7*box[0][0]//5, box[0][1]+6+len(passwd_txt)+1+len(passwd_input), "      ")
                    stdscr.move(7*box[0][0]//5, box[0][1]+6+len(passwd_txt)+1+len(passwd_input))
                elif len(passwd_input) < 20:
                    passwd_input = passwd_input + chr(key)
                    passwd_visible = passwd_visible + "*"
                    stdscr.addstr(7*box[0][0]//5, box[0][1]+6+len(passwd_txt)+len(passwd_input), "*")
        
        # Input para campo matricula
        while True:
            key = stdscr.getch()
            if key == curses.KEY_ENTER or key in [10, 13]:
                stdscr.move(9*box[0][0]//5, box[0][1]+6+len(carrera_txt)+1)
                break

            elif key == 8 or key == 127 or key == curses.KEY_BACKSPACE:
                matricula_input = matricula_input[:-1]
                stdscr.addstr(8*box[0][0]//5, box[0][1]+6+len(matricula_txt)+1+len(matricula_input), "   ")
                stdscr.move(8*box[0][0]//5, box[0][1]+6+len(matricula_txt)+1+len(matricula_input))

            else:
                if len(matricula_input) == 20:
                    stdscr.addstr(8*box[0][0]//5, box[0][1]+6+len(matricula_txt)+1+len(matricula_input), "   ")
                    stdscr.move(8*box[0][0]//5, box[0][1]+6+len(matricula_txt)+1+len(matricula_input))
                elif len(matricula_input) < 20:
                    matricula_input = matricula_input + chr(key)

        # Input para campo carrera
        while True:
            key = stdscr.getch()
            if key == curses.KEY_ENTER or key in [10, 13]:
                stdscr.move(9*box[0][0]//5, box[0][1]+6+len(carrera_txt)+1+len(carrera_input))
                break

            if key == 8 or key == 127 or key == curses.KEY_BACKSPACE:
                carrera_input = carrera_input[:-1]
                stdscr.addstr(9*box[0][0]//5, box[0][1]+6+len(carrera_txt)+1+len(carrera_input), "   ")
                stdscr.move(9*box[0][0]//5, box[0][1]+6+len(carrera_txt)+1+len(carrera_input))

            else:
                if len(carrera_input) == 20:
                    stdscr.addstr(9*box[0][0]//5, box[0][1]+6+len(carrera_txt)+1+len(carrera_input), "   ")
                    stdscr.move(9*box[0][0]//5, box[0][1]+6+len(carrera_txt)+1+len(carrera_input))
                elif len(carrera_input) < 20:
                    carrera_input = carrera_input + chr(key)


        cmd = 'python2 autenticar_cliente.py ' + user_input + ' ' + passwd_input
        shell = str(subprocess.check_output(cmd, shell=True).decode())
        auth = decode_auth_cliente(shell)
        stdscr.addstr(0,0, str(auth))

        if auth == '2':
            fail_login_txt = "Usuario o contrasena incorrecto, ingrese nuevamente"
            stdscr.addstr(max_y-3, (max_x//2)-len(fail_login_txt)//2, fail_login_txt)
            stdscr.addstr(6*box[0][0]//5, box[0][1]+6+len(user_txt)+1, "                         ")
            stdscr.addstr(7*box[0][0]//5, box[0][1]+6+len(passwd_txt)+1, "                         ")
            stdscr.addstr(8*box[0][0]//5, box[0][1]+6+len(matricula_txt)+1, "                         ")
            stdscr.addstr(9*box[0][0]//5, box[0][1]+6+len(carrera_txt)+1, "                         ")
            user_input = ""
            passwd_input = ""
            carrera_input = ""
            matricula_input = ""
            stdscr.move(6*box[0][0]//5, box[0][1]+6+len(user_txt)+1)

        if auth == '1':
            is_auth = True



    curses.noecho()
    curses.curs_set(0)
    bot_txt = "            Presione enter nuevamente              "

    #cmd = 'python2 autenticar_cliente.py ' + user_input + ' ' + passwd_input
    #subprocess.call(cmd, shell=True)

    stdscr.addstr(max_y-3, (max_x//2)-(len(bot_txt)//2), bot_txt)
    stdscr.getch()
    stdscr.refresh()

def authenticate_admin_menu(stdscr):
    stdscr.clear()
    max_y, max_x = stdscr.getmaxyx()
    box = [[max_y//3, max_x//3], [2*(max_y//3), 2*(max_x//3)]]
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

    title_txt = "Ingrese Credenciales"
    user_txt = "Usuario:"
    passwd_txt = "Contraseña:"

    user_input = ""
    passwd_input = ""
    passwd_visible = ""

    user = "admin"
    passwd = "admin"
    
    stdscr.addstr(box[0][0]-1, (max_x//2)-(len(title_txt)//2), title_txt, curses.color_pair(2))
    stdscr.addstr(4*box[0][0]//3, box[0][1]+6, user_txt, curses.color_pair(2))
    stdscr.addstr(5*box[0][0]//3, box[0][1]+6, passwd_txt, curses.color_pair(2))

    curses.curs_set(1)
    curses.echo()
    stdscr.move(4*box[0][0]//3, box[0][1]+6+len(user_txt)+1)

    is_auth = False

    while(is_auth != True):
        # Input para campo usuario
        while True:
            key = stdscr.getch()
            if key == curses.KEY_ENTER or key in [10, 13]:
                stdscr.move(5*box[0][0]//3, box[0][1]+6+len(passwd_txt)+1)
                break

            elif key == 8 or key == 127 or key == curses.KEY_BACKSPACE:
                    user_input = user_input[:-1]
                    stdscr.addstr(4*box[0][0]//3, box[0][1]+6+len(user_txt)+1+len(user_input), "   ")
                    stdscr.move(4*box[0][0]//3, box[0][1]+6+len(user_txt)+1+len(user_input))

            else:
                if len(user_input) == 20:
                    stdscr.addstr(4*box[0][0]//3, box[0][1]+6+len(user_txt)+1+len(user_input), " ")
                    stdscr.move(4*box[0][0]//3, box[0][1]+6+len(user_txt)+1+len(user_input))
                elif len(user_input) < 20:
                    user_input = user_input + chr(key)

        # Input para campo passwd
        while True:
            key = stdscr.getch()
            if key == curses.KEY_ENTER or key in [10, 13]:
                stdscr.move(5*box[0][0]//3, box[0][1]+6+len(passwd_txt)+1+len(passwd_input))
                break

            elif key == 8 or key == 127 or key == curses.KEY_BACKSPACE:
                passwd_input = passwd_input[:-1]
                stdscr.addstr(5*box[0][0]//3, box[0][1]+6+len(passwd_txt)+1+len(passwd_input), "   ")
                stdscr.move(5*box[0][0]//3, box[0][1]+6+len(passwd_txt)+1+len(passwd_input))

            else:
                if len(passwd_input) == 20:
                    stdscr.addstr(5*box[0][0]//3, box[0][1]+6+len(passwd_txt)+1+len(passwd_input), "      ")
                    stdscr.move(5*box[0][0]//3, box[0][1]+6+len(passwd_txt)+1+len(passwd_input))
                elif len(passwd_input) < 20:
                    passwd_input = passwd_input + chr(key)
                    passwd_visible = passwd_visible + "*"
                    stdscr.addstr(5*box[0][0]//3, box[0][1]+6+len(passwd_txt)+len(passwd_input), "*")

        if user_input != user or passwd_input != passwd:
            fail_login_txt = "Usuario o contrasena incorrecto, ingrese nuevamente"
            stdscr.addstr(max_y-3, (max_x//2)-len(fail_login_txt)//2, fail_login_txt)
            stdscr.addstr(4*box[0][0]//3, box[0][1]+6+len(user_txt)+1, "                         ")
            stdscr.addstr(5*box[0][0]//3, box[0][1]+6+len(passwd_txt)+1, "                         ")
            user_input = ""
            passwd_input = ""
            stdscr.move(4*box[0][0]//3, box[0][1]+6+len(user_txt)+1)

        elif user_input == user and passwd_input == passwd:
            is_auth = True
    

    curses.noecho()
    curses.curs_set(0)
    bot_txt = "            Presione enter nuevamente              "
    stdscr.addstr(max_y-3, (max_x//2)-(len(bot_txt)//2), bot_txt)
    stdscr.getch()
    stdscr.refresh()


def vote_menu(stdscr, vote_entries):
    stdscr.clear()
    max_y, max_x = stdscr.getmaxyx()
    mid_x = max_x//2
    n_op = len(vote_entries)
    title_txt = "Escoja una opcion"
    aviso_txt = "AVISO: Para navegar, utilize las flechas arriba/abajo."
    aviso2_txt = "Para seleccionar una opcion, presione 'x', y luego enter."
    vote_selection = 1
    i = 1
    stdscr.addstr((max_y//(n_op+2)), (mid_x)-(len(title_txt)//2), title_txt)
    stdscr.addstr(max_y-2, (mid_x)-(len(aviso_txt)//2), aviso_txt, curses.color_pair(2))
    stdscr.addstr(max_y-2+1, (mid_x)-(len(aviso2_txt)//2), aviso2_txt, curses.color_pair(2))

    for opcion in range(0,len(vote_entries)):
        i = i + 1
        y = (i*max_y//(n_op+2))
        if i == 2:
            stdscr.addstr(y, (max_x//4)-2, "X", curses.color_pair(2))

        stdscr.addstr(y, (max_x//4), "("+str(opcion+1)+") "+vote_entries[opcion])
        #stdscr.addstr(8+(x*2), mid_x-len(vote_options[x])//2, "("+str(x+1)+") "+vote_options[x])

    while True:
        key = stdscr.getch()
        stdscr.clear()
        i = 1

        stdscr.addstr((max_y//(n_op+2)), (mid_x)-(len(title_txt)//2), title_txt)
        stdscr.addstr(max_y-2, (mid_x)-(len(aviso_txt)//2), aviso_txt, curses.color_pair(2))
        stdscr.addstr(max_y-2+1, (mid_x)-(len(aviso2_txt)//2), aviso2_txt, curses.color_pair(2))

        if key == curses.KEY_UP and vote_selection > 1:
            vote_selection -= 1
        elif key == curses.KEY_DOWN and vote_selection < len(vote_entries):
            vote_selection += 1
        elif chr(key) == 'x' or chr(key) == 'X':
            opcion_txt = "Opcion {} seleccionada.".format(vote_selection)
            stdscr.addstr((max_y//(n_op+2))+2, (mid_x)-(len(opcion_txt)//2), opcion_txt)
            key = stdscr.getch()
            if key == curses.KEY_ENTER or key in [10, 13]:
                stdscr.clear()
                final_option_txt = "Usted ha votado por la opcion " + str(vote_selection) + ": " + vote_entries[vote_selection-1]
                gracias_txt = "Gracias por votar. Presione enter para terminar."
                stdscr.addstr(max_y//2, (max_x//2)-len(final_option_txt)//2, final_option_txt)
                stdscr.addstr((max_y//2)+3, (max_x//2)-len(gracias_txt)//2, gracias_txt)
                key = stdscr.getch()
                if key == curses.KEY_ENTER or key in [10, 13]:
                    break

        for opcion in vote_entries:
            i = i + 1
            y = (i*max_y//(n_op+2))
            stdscr.addstr(y, (max_x//4), opcion)

        y = ((vote_selection+1)*max_y)//(n_op+2)
        stdscr.addstr(y, (max_x//4)-2, 'X', curses.color_pair(2))
        stdscr.refresh()

def create_vote_menu(stdscr):
    stdscr.clear()
    max_y, max_x = stdscr.getmaxyx()
    mid_x = max_x//2

    vote_name_input = ""
    vote_options = ['Blanco', 'Nulo']
    num_op_input = ""

    header1_txt = "Ingese un nombre para la votacion:"
    stdscr.addstr(4, max_x//8, header1_txt, curses.color_pair(2))
    
    header2_txt = "Ingese cantidad de opciones (maximo 10), sin incluir blanco y nulo:"
    stdscr.addstr(7, max_x//8, header2_txt, curses.color_pair(2))

    curses.curs_set(1)
    curses.echo()
    stdscr.move(4, (max_x//8+len(header1_txt))+1)

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # Input para campo nombre
    while True:
        key = stdscr.getch()
        if key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.move(7, (max_x//8)+len(header2_txt)+1)
            break

        elif key == 8 or key == 127 or key == curses.KEY_BACKSPACE:
            vote_name_input = vote_name_input[:-1]
            stdscr.addstr(4, (max_x//8)+len(header1_txt)+2+len(vote_name_input)-1, "   ")
            stdscr.move(4, (max_x//8)+len(header1_txt)+2+len(vote_name_input)-1)

        else:
            if len(vote_name_input) == 20:
                stdscr.addstr(4, (max_x//8)+len(header1_txt)+2+len(vote_name_input)-1, "   ")
                stdscr.move(4, (max_x//8)+len(header1_txt)+2+len(vote_name_input)-1)
            elif len(vote_name_input) < 20:
                vote_name_input = vote_name_input + chr(key)


    valid = False
    while(valid != True):
        # Input para campo numero de opciones
        while True:
            key = stdscr.getch()
            if key == curses.KEY_ENTER or key in [10, 13]:
                if int(num_op_input) > 6 or int(num_op_input) <= 0:
                    stdscr.addstr(7, (max_x//8)+len(header2_txt)+len(num_op_input)+10, "Ingrese un numero correcto")
                    num_op_input = ""
                    stdscr.addstr(7, (max_x//8)+len(header2_txt)+1, "     ")
                    stdscr.move(7, (max_x//8)+len(header2_txt)+1)
                else:
                    valid = True
                    stdscr.addstr(7, (max_x//8)+len(header2_txt)+len(num_op_input)+10, "                            ")
                    break

            elif key == 8 or key == 127 or key == curses.KEY_BACKSPACE:
                num_op_input = num_op_input[:-1]
                stdscr.addstr(7, (max_x//8)+len(header2_txt)+2+len(num_op_input)-1, "   ")
                stdscr.move(7, (max_x//8)+len(header2_txt)+2+len(num_op_input)-1)

            else:
                if chr(key) in numbers:
                    if len(num_op_input) == 2:
                        stdscr.addstr(7, (max_x//8)+len(header2_txt)+2+len(num_op_input)-1, "   ")
                        stdscr.move(7, (max_x//8)+len(header2_txt)+2+len(num_op_input)-1)
                    elif len(num_op_input) < 2:
                        num_op_input = num_op_input + chr(key)
                else:
                    num_op_input = num_op_input + chr(key)
                    num_op_input = num_op_input[:-1]
                    stdscr.addstr(7, (max_x//8)+len(header2_txt)+2+len(num_op_input)-1, " ")
                    stdscr.move(7, (max_x//8)+len(header2_txt)+2+len(num_op_input)-1)

    stdscr.addstr(10, max_x//8, "Ingrese las opciones", curses.color_pair(2))

    for x in range(1, int(num_op_input)+1):
        stdscr.addstr(10+x*2, max_x//8, "Opcion ({}):".format(x))

    stdscr.move(12, (max_x//8)+len("Opcion (99): ")+1)

    op_input = ""
    for x in range(1, int(num_op_input)+1):
        while True:
            key = stdscr.getch()

            if key == curses.KEY_ENTER or key in [10, 13]:
                vote_options.append(op_input)
                op_input = ""
                stdscr.move(10+(x+1)*2, (max_x//8)+len("Opcion (99): ")+1)
                break

            elif key == 8 or key == 127 or key == curses.KEY_BACKSPACE:
                op_input = op_input[:-1]
                stdscr.addstr(10+x*2, (max_x//8)+len("Opcion (99): ")+len(op_input)+1, "   ")
                stdscr.move(10+x*2, (max_x//8)+len("Opcion (99): ")+len(op_input)+1)

            else:
                op_input = op_input + chr(key)

    stdscr.clear()
    final_txt = "Las opciones para la votacion son las siguientes:"
    stdscr.addstr(5, mid_x-len(final_txt)//2, final_txt, curses.color_pair(2))

    final2_txt = "Presione una tecla para confirmar"
    stdscr.addstr(max_y-4, mid_x-len(final2_txt)//2, final2_txt, curses.color_pair(2))

    for x in range(0, len(vote_options)):
        input_opc = str(x+1)+vote_options[x]
        cmd = 'python2 crear_opciones_cliente.py ' + input_opc
        shell = str(subprocess.check_output(cmd, shell=True).decode())
        stdscr.addstr(8+(x*2), mid_x-len(vote_options[x])//2, "("+str(x+1)+") "+vote_options[x])
        
    curses.curs_set(0)
    curses.noecho()
    stdscr.refresh()
    stdscr.getch()
    return vote_options

def show_results(stdscr):
    stdscr.clear()
    max_y, max_x = stdscr.getmaxyx()
    mid_x = max_x//2

    cmd = 'python2 contar_votos_cliente.py'
    shell = str(subprocess.check_output(cmd, shell=True).decode())
    vote_name, vote_results = decode_vote_results(shell)

    header_txt = "Resultados para la votacion: " + vote_name
    stdscr.addstr(2, mid_x-(len(header_txt)//2), header_txt, curses.color_pair(2))

    i = 0
    for result in vote_results:
        stdscr.addstr(8+(i*2), mid_x-(len(result)+len(str(vote_results[result])))//2, result + ": " + str(vote_results[result]))

        i = i + 1

    stdscr.refresh()
    stdscr.getch()


def main(stdscr):
    menu_entries = ['(1) Votar', '(2) Iniciar nueva votacion', '(3) Resultados', 'Salir']
    vote_entries = [' Opcion1', ' Opcion2', ' Opcion3', ' Opcion4', ' Opcion5']
    curses.curs_set(0)
    h, w = stdscr.getmaxyx()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

    header_win = curses.newwin(10, w-2, 2, 2)

    menu_selection = 0
    print_select_menu(stdscr, menu_selection, menu_entries)

    while True:
        print_header(header_win, w)
        header_win.refresh()
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and menu_selection > 0:
            menu_selection -= 1
        elif key == curses.KEY_DOWN and menu_selection < len(menu_entries) - 1:
            menu_selection += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            # Se selecciona la opcion salir
            if menu_selection == len(menu_entries) - 1:
                break
            # Se selecciona la opcion votar
            if menu_selection == 0:
                authenticate_vote_menu(stdscr)
                vote_menu(stdscr, vote_entries)
            # Se selecciona la opcion iniciar nueva votacion
            if menu_selection == 1:
                authenticate_admin_menu(stdscr)
                vote_entries =create_vote_menu(stdscr)
            # Se selecciona la opcion mostrar resultados
            if menu_selection == 2:
                show_results(stdscr)

            #stdscr.addstr(0, 0, "Opcion {} seleccionada.".format(menu_entries[menu_selection]))
            stdscr.refresh()

        print_select_menu(stdscr, menu_selection, menu_entries)

        stdscr.refresh()


curses.wrapper(main)