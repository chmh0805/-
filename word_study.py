from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import csv
import random

def load_words():
	user_file_name = simpledialog.askstring("input box", "파일명(.csv파일) :")
	user_file_name = str(user_file_name+".csv")
	try:
		load_file = open('./database/'+user_file_name, "r")
		for line in load_file.readlines():
			line = line.split(",")
			words[line[0]] = line[1][:-1]
		messagebox.showinfo("Complete", "불러오기 완료")
	except:
		messagebox.showinfo("Fail", "파일 이름을 확인해주세요!")


def quiz():
	f_wrong = open("./database/database_wrong.csv", 'a', newline='')
	wr_wrong = csv.writer(f_wrong)
	quest_word_list = list(words.keys())
	while True:
		if len(quest_word_list) == 0:
			messagebox.showinfo("None", "단어장에 단어가 없습니다.")
			break
		else:
			quest_word = str(random.choice(quest_word_list))
			quest_answer = str(words[quest_word])
			user_answer = simpledialog.askstring("Quiz !", quest_word+": \n종료하려면 quit을 입력하세요.")
			if user_answer == quest_answer:
				messagebox.showinfo("Correct!", "정답입니다 !")
				del words[quest_word]
				quest_word_list.remove(quest_word)
			elif user_answer.lower() == "quit":
				messagebox.showinfo("Quit", "퀴즈를 종료합니다.")
				break
			else:
				messagebox.showinfo("Wrong!", "틀렸습니다. 정답은 {}입니다.".format(quest_answer))
				wr_wrong.writerow([quest_word, quest_answer])
				del words[quest_word]
				quest_word_list.remove(quest_word)


def reset_words():
	user_again = simpledialog.askstring("Data Reset", "정말 초기화하시겠습니까?(y/n)")
	if user_again.upper() == 'Y':
		words = dict()
		with open("./database/database.csv", 'w') as f0:
			pass
		messagebox.showinfo("", "초기화 완료")
	else:
		messagebox.showinfo("", "초기화하지 않았습니다.")


def wrong_words():
	user_wrong_again = simpledialog.askstring("Wrong Words", "정말 불러오시겠습니까?(y/n)")
	if user_wrong_again.upper() == 'Y':
		with open("./database/database_wrong.csv", 'r') as f3:
			rdr_wrong = csv.reader(f3)
			for line in rdr_wrong:
				if line == []:
					pass
				elif line[0] not in words.keys():
					words[line[0]] = line[1]
			messagebox.showinfo("", "불러오기 완료")
	else:
		messagebox.showinfo("", "불러오지 않았습니다.")
	with open("./database/database_wrong.csv", 'w') as f4:
		pass


def check_word_num():
	messagebox.showinfo("", str(len(words.keys())) + "개 남았습니다. 화이팅!")


def quit():
	with open("./database/database.csv", 'a', newline='') as f_quit:
		wr = csv.writer(f_quit)
		for quit_word, meaning in words.items():
			w_l = [quit_word, meaning]
			wr.writerow(w_l)
	win.destroy()


win = Tk()
win.geometry("800x500")
win.title("Word Study - Made by chmh0805(Naver)/h_ggob(Insta)")
win.option_add("*Font", "맑은고딕 20")

words = {}
with open("./database/database.csv", 'r') as f1:
	rdr = csv.reader(f1)
	for line in rdr:
		if line != []:
			words[line[0]] = line[1]

btn1 = Button(win, text="단어 불러오기", command=load_words)
btn1.place(x=250, y=25, width=320, height=70)

btn2 = Button(win, text="퀴즈 시작", command=quiz)
btn2.place(x=250, y=115, width=320, height=70)

btn3 = Button(win, text="저장된 단어 초기화", command=reset_words)
btn3.place(x=250, y=205, width=320, height=70)

btn4 = Button(win, text="틀린 단어만 불러오기", command=wrong_words)
btn4.place(x=250, y=295, width=320, height=70)

btn5 = Button(win, text="현재 남은 단어 갯수 확인", command=check_word_num)
btn5.place(x=250, y=385, width=320, height=70)

btn_quit = Button(win, text="종료", command=quit)
btn_quit.place(x=740, y=0, width=60, height=30)

win.mainloop()