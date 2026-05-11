import tkinter as tk
from tkinter import messagebox, ttk
import random
from fractions import Fraction

class MathTrainer:
    def __init__(self, root):
        self.root = root
        self.root.title("Тренажёр")
        self.root.geometry("650x550")
        self.root.resizable(True, True)
        
        # Переменная для полноэкранного режима
        self.fullscreen = False
        
        # Тема (dark или light)
        self.theme = "light"
        
        # Состояние
        self.screen = "category"
        self.category = None
        self.level = 1
        self.score = 0
        self.total = 0
        self.problem = None
        self.feedback = None
        
        # Цвета для тем
        self.colors = {
            "light": {
                "bg": "#f5f5f5",
                "fg": "#333333",
                "button": "#4CAF50",
                "button_fg": "white",
                "entry": "white",
                "entry_fg": "#333333",
                "title": "#2196F3",
                "frame": "white",
                "frame_fg": "#333333",
                "button_secondary": "#f44336"
            },
            "dark": {
                "bg": "#1e1e1e",
                "fg": "#ffffff",
                "button": "#2196F3",
                "button_fg": "white",
                "entry": "#2d2d2d",
                "entry_fg": "#ffffff",
                "title": "#64B5F6",
                "frame": "#2d2d2d",
                "frame_fg": "#ffffff",
                "button_secondary": "#d32f2f"
            }
        }
        
        # Главный фрейм
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Верхняя панель с кнопками
        self.top_bar = tk.Frame(self.main_frame)
        self.top_bar.pack(fill=tk.X, pady=10, padx=10)
        
        # Кнопка полноэкранного режима
        self.fullscreen_btn = tk.Button(self.top_bar, text="Полный экран", command=self.toggle_fullscreen)
        self.fullscreen_btn.pack(side=tk.RIGHT, padx=5)
        
        # Кнопка темы
        self.theme_btn = tk.Button(self.top_bar, text="Тёмная тема", command=self.toggle_theme)
        self.theme_btn.pack(side=tk.RIGHT, padx=5)
        
        # Контентный фрейм
        self.content_frame = tk.Frame(self.main_frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Применяем тему
        self.apply_theme()
        
        self.show_category()
        
        # Привязываем клавишу F11 для полноэкранного режима
        self.root.bind("<F11>", lambda event: self.toggle_fullscreen())
        self.root.bind("<Escape>", lambda event: self.exit_fullscreen())
    
    def toggle_fullscreen(self):
        """Переключение полноэкранного режима"""
        self.fullscreen = not self.fullscreen
        self.root.attributes("-fullscreen", self.fullscreen)
        if self.fullscreen:
            self.fullscreen_btn.config(text="Выйти")
        else:
            self.fullscreen_btn.config(text="Полный экран")
    
    def exit_fullscreen(self):
        """Выход из полноэкранного режима"""
        if self.fullscreen:
            self.fullscreen = False
            self.root.attributes("-fullscreen", False)
            self.fullscreen_btn.config(text="Полный экран")
    
    def apply_theme(self):
        """Применение текущей темы"""
        colors = self.colors[self.theme]
        
        # Основные цвета
        self.root.configure(bg=colors["bg"])
        self.main_frame.configure(bg=colors["bg"])
        self.top_bar.configure(bg=colors["bg"])
        self.content_frame.configure(bg=colors["bg"])
        
        # Кнопка темы
        if self.theme == "light":
            self.theme_btn.config(text="Тёмная тема", bg=colors["button"], fg=colors["button_fg"])
        else:
            self.theme_btn.config(text="Светлая тема", bg=colors["button"], fg=colors["button_fg"])
        
        # Перерисовываем текущий экран
        self.refresh_screen()
    
    def toggle_theme(self):
        """Переключение темы"""
        self.theme = "dark" if self.theme == "light" else "light"
        self.apply_theme()
    
    def refresh_screen(self):
        """Обновление текущего экрана"""
        if self.screen == "category":
            self.show_category()
        elif self.screen == "level":
            self.show_level()
        elif self.screen == "game":
            self.show_game()
        elif self.screen == "result":
            self.show_result()
    
    def get_question_count(self, level):
        if level <= 2:
            return 5
        elif level == 3:
            return 6
        elif level == 4:
            return 8
        else:
            return 10
    
    def generate_normal(self, level):
        if level == 1:
            a, b = random.randint(1, 10), random.randint(1, 10)
        elif level == 2:
            a, b = random.randint(10, 30), random.randint(1, 20)
        elif level == 3:
            a, b = random.randint(20, 80), random.randint(10, 50)
        elif level == 4:
            a, b = random.randint(50, 200), random.randint(10, 100)
        else:
            a, b = random.randint(100, 500), random.randint(10, 200)
        
        op = random.choice(["+", "-", "*", "/"])
        if op == "/":
            a = b * random.randint(1, 10)
        
        result = Fraction(eval(f"{a}{op}{b}"))
        return a, b, result, op
    
    def generate_fraction(self, level):
        # Везде делаем одинаковые знаменатели
        if level <= 2:
            b = random.randint(2, 10)
            a = random.randint(1, 10)
            c = random.randint(1, 10)
            op = random.choice(["+", "-"])
        elif level <= 3:
            b = random.randint(10, 99)
            a = random.randint(10, 99)
            c = random.randint(10, 99)
            op = random.choice(["+", "-", "*"])
        else:
            b = random.randint(100, 500)
            a = random.randint(100, 500)
            c = random.randint(100, 500)
            op = random.choice(["+", "-", "*", "/"])
        
        f1 = Fraction(a, b)
        f2 = Fraction(c, b)  # одинаковый знаменатель
        
        if op == "+":
            result = f1 + f2
        elif op == "-":
            result = f1 - f2
        elif op == "*":
            result = f1 * f2
        else:
            result = f1 / f2
        
        return a, b, c, op, result
    
    def generate_problem(self):
        if self.category == "Обычные":
            return self.generate_normal(self.level)
        else:
            return self.generate_fraction(self.level)
    
    def clear_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def show_category(self):
        self.clear_frame()
        colors = self.colors[self.theme]
        
        # Заголовок
        title = tk.Label(self.content_frame, text="Меню", font=("Arial", 28, "bold"), 
                        bg=colors["bg"], fg=colors["title"])
        title.pack(pady=30)
        
        # Рамка для выбора
        frame = tk.Frame(self.content_frame, bg=colors["frame"], relief=tk.RAISED, bd=2)
        frame.pack(pady=30, padx=50, fill=tk.BOTH)
        
        tk.Label(frame, text="Выберите тип заданий:", font=("Arial", 14), 
                bg=colors["frame"], fg=colors["frame_fg"]).pack(pady=20)
        
        # Стилизованные кнопки выбора
        btn_style = {"width": 20, "height": 2, "font": ("Arial", 12)}
        
        normal_btn = tk.Button(frame, text="Обычные числа", 
                              command=lambda: self.select_category("Обычные"),
                              bg=colors["button"], fg=colors["button_fg"],
                              **btn_style)
        normal_btn.pack(pady=10)
        
        fraction_btn = tk.Button(frame, text="Дроби", 
                                command=lambda: self.select_category("Дроби"),
                                bg=colors["button"], fg=colors["button_fg"],
                                **btn_style)
        fraction_btn.pack(pady=10)
        
        # Кнопка далее
        self.next_btn = tk.Button(self.content_frame, text="Далее", command=self.next_to_level,
                                 font=("Arial", 12), bg=colors["button"], fg=colors["button_fg"],
                                 width=15, height=1)
        self.next_btn.pack(pady=20)
    
    def select_category(self, category):
        self.category = category
        messagebox.showinfo("Выбрано", f"Выбрано: {category}")
    
    def next_to_level(self):
        if self.category:
            self.screen = "level"
            self.show_level()
        else:
            messagebox.showwarning("Внимание", "Сначала выберите тип заданий!")
    
    def show_level(self):
        self.clear_frame()
        colors = self.colors[self.theme]
        
        title = tk.Label(self.content_frame, text="Выберите сложность", 
                        font=("Arial", 24, "bold"), bg=colors["bg"], fg=colors["title"])
        title.pack(pady=30)
        
        # Информация об уровнях
        info_frame = tk.Frame(self.content_frame, bg=colors["frame"], relief=tk.GROOVE, bd=2)
        info_frame.pack(pady=20, padx=30, fill=tk.X)
        
        levels_info = [
            "1 уровень: 5 примеров (Числа 1-10)",
            "2 уровень: 5 примеров (Числа 10-30)",
            "3 уровень: 6 примеров (Числа 20-80)",
            "4 уровень: 8 примеров (Числа 50-200)",
            "5 уровень: 10 примеров (Числа 100-500)"
        ]
        
        for info in levels_info:
            tk.Label(info_frame, text=info, font=("Arial", 10), 
                    bg=colors["frame"], fg=colors["frame_fg"]).pack(pady=2)
        
        # Ползунок уровня
        self.level_var = tk.IntVar(value=1)
        level_slider = tk.Scale(self.content_frame, from_=1, to=5, orient=tk.HORIZONTAL,
                                variable=self.level_var, length=400, font=("Arial", 12),
                                bg=colors["bg"], fg=colors["fg"], 
                                troughcolor=colors["button"], highlightthickness=0)
        level_slider.pack(pady=20)
        
        # Текущий уровень
        self.level_label = tk.Label(self.content_frame, text="Текущий уровень: 1", 
                                   font=("Arial", 12), bg=colors["bg"], fg=colors["fg"])
        self.level_label.pack()
        
        def update_level(*args):
            self.level_label.config(text=f"Текущий уровень: {self.level_var.get()}")
        
        self.level_var.trace("w", update_level)
        
        # Кнопки
        btn_frame = tk.Frame(self.content_frame, bg=colors["bg"])
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="Начать", command=self.start_game,
                 font=("Arial", 12), bg=colors["button"], fg=colors["button_fg"],
                 width=12).pack(side=tk.LEFT, padx=10)
        
        tk.Button(btn_frame, text="Назад", command=self.show_category,
                 font=("Arial", 12), bg=colors["button_secondary"], fg=colors["button_fg"],
                 width=12).pack(side=tk.LEFT, padx=10)
    
    def start_game(self):
        self.level = self.level_var.get()
        self.screen = "game"
        self.score = 0
        self.total = 0
        self.problem = None
        self.feedback = None
        self.show_game()
    
    def show_game(self):
        self.clear_frame()
        colors = self.colors[self.theme]
        
        max_q = self.get_question_count(self.level)
        
        if self.total >= max_q:
            self.show_result()
            return
        
        if self.problem is None:
            self.problem = self.generate_problem()
        
        # Верхняя панель с прогрессом
        progress_frame = tk.Frame(self.content_frame, bg=colors["frame"], relief=tk.FLAT)
        progress_frame.pack(fill=tk.X, pady=10)
        
        # Прогресс-бар
        progress = self.total / max_q
        progress_bar = ttk.Progressbar(progress_frame, length=400, mode='determinate', 
                                       value=progress*100)
        progress_bar.pack(pady=10)
        
        stats_text = f"Вопрос {self.total + 1}/{max_q} | Правильных: {self.score}"
        stats_label = tk.Label(progress_frame, text=stats_text, font=("Arial", 12),
                              bg=colors["frame"], fg=colors["frame_fg"])
        stats_label.pack()
        
        # Карточка с заданием
        task_frame = tk.Frame(self.content_frame, bg=colors["frame"], relief=tk.RAISED, bd=3)
        task_frame.pack(pady=30, padx=40, fill=tk.BOTH, expand=True)
        
        if self.category == "Обычные":
            a, b, correct, op = self.problem
            task_text = f"{a} {op} {b}"
            task_label = tk.Label(task_frame, text=task_text, font=("Arial", 48, "bold"),
                                 bg=colors["frame"], fg=colors["title"])
            task_label.pack(expand=True)
            
            eq_label = tk.Label(task_frame, text="= ?", font=("Arial", 36),
                               bg=colors["frame"], fg=colors["frame_fg"])
            eq_label.pack()
        else:
            a, b, c, op, correct = self.problem
            
            # Создаем горизонтальный фрейм для размещения двух дробей и операции
            fractions_frame = tk.Frame(task_frame, bg=colors["frame"])
            fractions_frame.pack(expand=True)
            
            # Первая дробь
            frac1_frame = tk.Frame(fractions_frame, bg=colors["frame"])
            frac1_frame.pack(side=tk.LEFT, padx=20)
            
            num1 = tk.Label(frac1_frame, text=str(a), font=("Arial", 32, "bold"),
                           bg=colors["frame"], fg=colors["title"])
            num1.pack()
            
            line1 = tk.Frame(frac1_frame, height=3, bg=colors["frame_fg"], width=60)
            line1.pack(pady=5)
            
            den1 = tk.Label(frac1_frame, text=str(b), font=("Arial", 32),
                           bg=colors["frame"], fg=colors["frame_fg"])
            den1.pack()
            
            # Знак операции
            op_label = tk.Label(fractions_frame, text=f" {op} ", font=("Arial", 36, "bold"),
                               bg=colors["frame"], fg=colors["frame_fg"])
            op_label.pack(side=tk.LEFT, padx=20)
            
            # Вторая дробь
            frac2_frame = tk.Frame(fractions_frame, bg=colors["frame"])
            frac2_frame.pack(side=tk.LEFT, padx=20)
            
            num2 = tk.Label(frac2_frame, text=str(c), font=("Arial", 32, "bold"),
                           bg=colors["frame"], fg=colors["title"])
            num2.pack()
            
            line2 = tk.Frame(frac2_frame, height=3, bg=colors["frame_fg"], width=60)
            line2.pack(pady=5)
            
            den2 = tk.Label(frac2_frame, text=str(b), font=("Arial", 32),
                           bg=colors["frame"], fg=colors["frame_fg"])
            den2.pack()
            
            # Знак равно
            eq_label = tk.Label(task_frame, text="= ?", font=("Arial", 28),
                               bg=colors["frame"], fg=colors["frame_fg"])
            eq_label.pack(pady=20)
        
        # Поле ввода
        input_frame = tk.Frame(self.content_frame, bg=colors["bg"])
        input_frame.pack(pady=20)
        
        tk.Label(input_frame, text="Ваш ответ:", font=("Arial", 14),
                bg=colors["bg"], fg=colors["fg"]).pack()
        
        self.answer_entry = tk.Entry(input_frame, font=("Arial", 16), width=20,
                                     bg=colors["entry"], fg=colors["entry_fg"],
                                     insertbackground=colors["fg"])
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind("<Return>", lambda event: self.check_answer())
        
        # Кнопки
        btn_frame = tk.Frame(self.content_frame, bg=colors["bg"])
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Проверить", command=self.check_answer,
                 font=("Arial", 12), bg="#4CAF50", fg="white",
                 width=12).pack(side=tk.LEFT, padx=10)
        
        tk.Button(btn_frame, text="В меню", command=self.show_category,
                 font=("Arial", 12), bg=colors["button_secondary"], fg=colors["button_fg"],
                 width=12).pack(side=tk.LEFT, padx=10)
        
        # Фокус на поле ввода
        self.answer_entry.focus()
    
    def check_answer(self):
        answer = self.answer_entry.get()
        
        if not answer:
            messagebox.showwarning("Внимание", "Введите ответ!")
            return
        
        try:
            if self.category == "Обычные":
                a, b, correct, op = self.problem
            else:
                a, b, c, op, correct = self.problem
            
            correct_answer = Fraction(correct)
            user_answer = Fraction(answer)
            
            if user_answer == correct_answer:
                self.feedback = "Правильно!"
                self.score += 1
            else:
                self.feedback = f"Неправильно.\nОтвет: {correct_answer}"
        except:
            self.feedback = "Ошибка!\nВведите число или дробь (например: 1/2)"
        
        self.total += 1
        self.problem = None
        
        # Показываем результат
        messagebox.showinfo("Результат", self.feedback)
        
        # Обновляем экран
        self.show_game()
    
    def show_result(self):
        self.clear_frame()
        colors = self.colors[self.theme]
        
        max_q = self.get_question_count(self.level)
        percent = (self.score / max_q) * 100
        
        # Оценка
        if percent == 100:
            grade = "Отлично!"
        elif percent >= 80:
            grade = "Хорошо!"
        elif percent >= 60:
            grade = "Неплохо!"
        else:
            grade = "Нужно ещё потренироваться!"
        
        title = tk.Label(self.content_frame, text="Результат", 
                        font=("Arial", 28, "bold"), bg=colors["bg"], fg=colors["title"])
        title.pack(pady=20)
        
        # Результаты
        result_frame = tk.Frame(self.content_frame, bg=colors["frame"], relief=tk.RAISED, bd=2)
        result_frame.pack(pady=30, padx=40, fill=tk.BOTH)
        
        tk.Label(result_frame, text="Правильных ответов:", font=("Arial", 16),
                bg=colors["frame"], fg=colors["frame_fg"]).pack(pady=10)
        
        tk.Label(result_frame, text=f"{self.score} / {max_q}", font=("Arial", 36, "bold"),
                bg=colors["frame"], fg=colors["title"]).pack(pady=10)
        
        tk.Label(result_frame, text=f"Процент: {percent:.1f}%", font=("Arial", 14),
                bg=colors["frame"], fg=colors["frame_fg"]).pack(pady=10)
        
        tk.Label(result_frame, text=grade, font=("Arial", 14, "bold"),
                bg=colors["frame"], fg=colors["title"]).pack(pady=10)
        
        # Кнопки
        btn_frame = tk.Frame(self.content_frame, bg=colors["bg"])
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="Сыграть снова", command=self.play_again,
                 font=("Arial", 12), bg=colors["button"], fg=colors["button_fg"],
                 width=15).pack(side=tk.LEFT, padx=10)
        
        tk.Button(btn_frame, text="В меню", command=self.show_category,
                 font=("Arial", 12), bg=colors["button_secondary"], fg=colors["button_fg"],
                 width=15).pack(side=tk.LEFT, padx=10)
    
    def play_again(self):
        self.start_game()

# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = MathTrainer(root)
    root.mainloop()