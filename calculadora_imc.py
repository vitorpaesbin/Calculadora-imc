import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox


historico = []

def calcular_imc():
    try:
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())
        imc = peso / (altura ** 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"

        resultado = f"IMC: {imc:.2f} - {classificacao}"
        historico.append(resultado)
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Erro", "Insira valores válidos para peso e altura.")

def mostrar_historico():
    if not historico:
        messagebox.showinfo("Histórico", "Nenhum cálculo realizado ainda.")
        return

    janela_hist = ttk.Toplevel(janela)
    janela_hist.title("Histórico de IMC")
    janela_hist.geometry("300x200")

    texto = ttk.Text(janela_hist, wrap="word")
    texto.pack(expand=True, fill="both", padx=10, pady=10)

    for item in historico:
        texto.insert("end", item + "\n")

# Tema moderno: "flatly", "darkly", "cyborg", "journal", "solar", etc.
janela = ttk.Window(themename="flatly")
janela.title("Calculadora de IMC")
janela.geometry("320x280")
janela.resizable(False, False)



frame = ttk.Frame(janela, padding=15)
frame.pack(expand=True)

ttk.Label(frame, text="Peso (kg):", font=("Segoe UI", 10)).pack(anchor="w")
entrada_peso = ttk.Entry(frame)
entrada_peso.pack(fill="x", pady=5)

ttk.Label(frame, text="Altura (m):", font=("Segoe UI", 10)).pack(anchor="w")
entrada_altura = ttk.Entry(frame)
entrada_altura.pack(fill="x", pady=5)

frame_botoes = ttk.Frame(frame)
frame_botoes.pack(pady=10, fill="x")

ttk.Button(frame_botoes, text="Calcular IMC", bootstyle=SUCCESS, command=calcular_imc).pack(side="left", expand=True, fill="x", padx=5)
ttk.Button(frame_botoes, text="Ver Histórico", bootstyle=INFO, command=mostrar_historico).pack(side="left", expand=True, fill="x", padx=5)


janela.mainloop()