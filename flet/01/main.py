import flet as ft

#vars
operaca = ""
n1 = []
n2 = []
is_n1 = True

def main(page: ft.Page):
    text_n = ft.Text(value="0", size=20)
    
    def default():
        global is_n1
        text_n.value = "0"
        #limpa as lista
        n1.clear()
        n2.clear()
        is_n1 = True
        return
    
    #trata os erros
    def get_txt(_n: str):
        try:
            if "," in _n:
                return float(_n.replace(",", "."))
            else:
                return int(_n)
        except ValueError:
            return 0

    def AC(e):
        default()
        text_n.update()

    def negative(e):
        global n1, n2, is_n1
        #ver qual é o número qua vai ser alterado
        if is_n1:
            _n = get_txt("".join(n1))
            #ver se ele 0
            if _n != 0:
                _n *= -1
                n1 = list(str(_n).replace(".", ","))
                text_n.value = "".join(n1)
        else:
            _n = get_txt("".join(n2))
            if _n != 0:
                _n *= -1
                n2 = list(str(_n).replace(".", ","))
                text_n.value = "".join(n2)
        
        text_n.update()

    def virgula(e):
        global n1, n2, is_n1

        #ver qual número tem virgula
        if is_n1:
            #ver ser já tem virgula
            if "," not in n1:
                #ver ser já tem algo inserido
                if not n1: 
                    n1.append("0")
                n1.append(",")
            text_n.value = "".join(n1)
        else:
            if "," not in n2:
                if not n2:
                    n2.append("0")
                n2.append(",")
            text_n.value = "".join(n2)

        text_n.update()

    def teclado(e):
        if is_n1:
            #pega o nome do button
            n1.append(e.control.text)
            text_n.value = "".join(n1)
            text_n.update()
        else:
            n2.append(e.control.text)
            text_n.value = "".join(n2)
            text_n.update()
            
    def soma(e):
        global operaca, is_n1
        operaca = "+"
        is_n1 = False
        text_n.value = "0"
        text_n.update()

    def div(e):
        global operaca, is_n1
        operaca = "/"
        is_n1 = False
        text_n.value = "0"
        text_n.update()

    def multi(e):
        global operaca, is_n1
        operaca = "x"
        is_n1 = False
        text_n.value = "0"
        text_n.update()

    def sub(e):
        global operaca, is_n1
        operaca = "-"
        is_n1 = False
        text_n.value = "0"
        text_n.update()

    def igual(e):
        global n1, n2, operaca, is_n1
        
        _n1 = get_txt("".join(n1))
        _n2 = get_txt("".join(n2))

        match operaca:
            case "+":
                text_n.value = _n1 + _n2

            case "-":
                text_n.value = _n1 - _n2

            case "x":
                text_n.value = _n1 * _n2

            case "/":
                if _n2 != 0:
                    text_n.value = _n1 / _n2

                else:
                    text_n.value = "imposivel dividi por 0"
        text_n.update()

    page.add(
        ft.Row(controls=[text_n]),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="AC", on_click=AC),
                ft.ElevatedButton(text="+/-", on_click=negative),
                ft.ElevatedButton(text="%", on_click=...),
                ft.ElevatedButton(text="/", on_click=div),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="7", on_click=teclado),
                ft.ElevatedButton(text="8", on_click=teclado),
                ft.ElevatedButton(text="9", on_click=teclado),
                ft.ElevatedButton(text="x",on_click=multi),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="4", on_click=teclado),
                ft.ElevatedButton(text="5", on_click=teclado),
                ft.ElevatedButton(text="6", on_click=teclado),
                ft.ElevatedButton(text="-",on_click=sub),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="1", on_click=teclado),
                ft.ElevatedButton(text="2", on_click=teclado),
                ft.ElevatedButton(text="3", on_click=teclado),
                ft.ElevatedButton(text="+", on_click=soma),
            ]
        ),
        ft.Row(
             controls=[
                ft.ElevatedButton(text="0", on_click=teclado),
                ft.ElevatedButton(text=",", on_click=virgula),
                ft.ElevatedButton(text="=", on_click=igual),
            ]
        ),
    )   

ft.app(main)