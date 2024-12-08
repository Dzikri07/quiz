import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
from tkinter import *
import pygame
import os

# Path gambar yang digunakan
image_path = "C:/Users/Dzikr/Documents/projectpy/img/soal1.jpg"
if os.path.exists(image_path):
    print("Gambar ditemukan!")
else:
    print("Gambar tidak ditemukan!")



# Soal dengan nama file gambar soal1.jpg hingga soal10.jpg
questions = [
    {
        "question": "Apa penyebab utama sifilis?",
        "options": ["Virus HIV", "Bakteri Treponema pallidum", "Jamur Candida", "Parasit Plasmodium"],
        "answer": "Bakteri Treponema pallidum",
        "image": "img/soal1.jpg"
    },
    {
        "question": "Sifilis dikenal juga sebagai penyakit apa?",
        "options": ["Penyakit gonore", "Penyakit raja singa", "Penyakit herpes", "Penyakit klamidia"],
        "answer": "Penyakit raja singa",
        "image": "img/soal2.jpg"
    },
    {
        "question": "Bagaimana cara utama penularan sifilis?",
        "options": ["Melalui udara", "Melalui kontak seksual", "Melalui makanan", "Melalui air"],
        "answer": "Melalui kontak seksual",
        "image": "img/soal3.jpg"
    },
    {
        "question": "Apa gejala awal yang umum muncul pada sifilis?",
        "options": ["Demam tinggi", "Luka tidak nyeri pada area kelamin", "Batuk berkepanjangan", "Nyeri kepala"],
        "answer": "Luka tidak nyeri pada area kelamin",
        "image": "img/soal4.jpg"
    },
    {
        "question": "Apa yang dapat terjadi jika sifilis tidak diobati?",
        "options": ["Sembuh dengan sendirinya", "Penyakit akan tetap tidak aktif selamanya", "Kerusakan pada organ vital", "Tidak ada efek"],
        "answer": "Kerusakan pada organ vital",
        "image": "img/soal5.jpg"
    },
    {
        "question": "Siapa yang memiliki risiko tinggi terinfeksi sifilis?",
        "options": ["Orang yang tidak merokok", "Wanita hamil", "Pekerja seks komersial", "Semua di atas"],
        "answer": "Semua di atas",
        "image": "img/soal6.jpg"
    },
    {
        "question": "Apa tahap pertama dari infeksi sifilis?",
        "options": ["Sifilis sekunder", "Sifilis tersier", "Masa inkubasi", "Sifilis primer"],
        "answer": "Sifilis primer",
        "image": "img/soal7.jpg"
    },
    {
        "question": "Apa yang dimaksud dengan sifilis kongenital?",
        "options": ["Sifilis yang ditularkan melalui transfusi darah", 
                    "Sifilis yang ditularkan dari ibu ke bayi selama kehamilan",
                    "Sifilis yang disebabkan oleh jamur", 
                    "Sifilis yang tidak menular"],
        "answer": "Sifilis yang ditularkan dari ibu ke bayi selama kehamilan",
        "image": "img/soal8.jpg"
    },
    {
        "question": "Apa yang menjadi tujuan WHO terkait dengan sifilis pada tahun 2030?",
        "options": ["Meningkatkan jumlah kasus", 
                    "Menurunkan kasus sifilis sebanyak 90%", 
                    "Menghapus sifilis dari dunia", 
                    "Meningkatkan pengobatan"],
        "answer": "Menurunkan kasus sifilis sebanyak 90%",
        "image": "img/soal9.jpg"
    },
    {
        "question": "Apa tindakan pencegahan utama terhadap sifilis?",
        "options": ["Menghindari olahraga", "Menggunakan kondom saat berhubungan seksual", "Menjaga pola makan", "Banyak tidur"],
        "answer": "Menggunakan kondom saat berhubungan seksual",
        "image": "img/soal10.jpg"
    }
]

current_question_index = 0
score = 0

def check_answer(selected_option):
    global current_question_index, score
    correct_answer = questions[current_question_index]["answer"]
    if selected_option == correct_answer:
        score += 1
        messagebox.showinfo("Benar!", "Jawaban kamu benar!")
    else:
        messagebox.showerror("Salah!", f"Jawaban kamu salah. Jawaban yang benar: {correct_answer}")
    
    current_question_index += 1
    if current_question_index < len(questions):
        load_question()
    else:
        messagebox.showinfo("Hasil", f"Kuis selesai! Skor kamu: {score}/{len(questions)}")
        root.destroy()

def load_question():
    question_label.config(text=f"{current_question_index + 1}. {questions[current_question_index]['question']}")
    
    # Gunakan path dinamis untuk gambar
    image_path = resource_path(questions[current_question_index]["image"])
    try:
        # Load dan tampilkan gambar
        img = Image.open(image_path).resize((200, 200))  # Sesuaikan ukuran gambar
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk
    except FileNotFoundError:
        messagebox.showerror("Error", f"Gambar {image_path} tidak ditemukan.")
    
    # Update opsi jawaban
    for i, option in enumerate(questions[current_question_index]["options"]):
        option_buttons[i].config(text=option, command=lambda opt=option: check_answer(opt))

# Fungsi resource_path untuk mendukung path dinamis
def resource_path(relative_path):
    """Dapatkan path absolut ke resource, mendukung mode pengembangan dan bundling"""
    if getattr(sys, '_MEIPASS', False):  # Saat dijalankan sebagai exe
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

pygame.mixer.init()

def play():
    pygame.mixer_music.load("music\bgm.mp3")
    pygame.mixer.music.play(loops=0)

root = tk.Tk()
root.title("Kuis Sifilis")
root.geometry("600x500")

question_label = tk.Label(root, text="", wraplength=500, font=("Arial", 14), justify="center")
question_label.pack(pady=10)

image_label = tk.Label(root)
image_label.pack(pady=10)

option_buttons = []
for _ in range(4):
    button = tk.Button(root, text="", font=("Arial", 12), width=50, command=None)
    button.pack(pady=5)
    option_buttons.append(button)

load_question()

root.mainloop()
