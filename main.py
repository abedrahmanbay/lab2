import os
import time
import math
from typing import List

# --- 0. Последовательность чисел (Чтение из файла sequence.txt) ---
def get_sequence_data() -> List[float]:
    """
    Считывает последовательность чисел из локального файла 'sequence.txt'.
    """
    numbers = []
    
    try:
        with open('sequence.txt', 'r') as file:
            data_text = file.read()
            
            for item in data_text.split():
                try:
                    numbers.append(float(item))
                except ValueError:
                    continue
                    
    except FileNotFoundError:
        print("❌ Ошибка: Файл 'sequence.txt' не найден.")
        print("Пожалуйста, создайте файл и поместите его в ту же папку, что и скрипт.")
        return []
    except Exception as e:
        print(f"❌ Произошла ошибка при чтении файла: {e}")
        return []
        
    return numbers


# --- 1. Флаг Польши ---
def draw_polish_flag():
    print("## 🇵🇱 1. Флаг Польши (Бело-Красный)")
    
    WHITE_BG_RED_TEXT = '\033[47m\033[31m'
    RED_BG_WHITE_TEXT = '\033[41m\033[37m'
    RESET = '\033[0m'
    
    block = '██' 
    width = 15 
    
    for _ in range(3):
        print(f"{WHITE_BG_RED_TEXT}{block * width}{RESET}")
        
    for _ in range(3):
        print(f"{RED_BG_WHITE_TEXT}{block * width}{RESET}")


# --- 2. Повторяющийся узор 'd' (исправленная версия с ASCII) ---
def draw_d_pattern():
    print("\n" + "-" * 30)
    print("## 🔡 2. Повторяющийся узор 'd'")
    
    # Используем обычные символы ASCII вместо блоков
    pattern_lines = [
        " ######## ",
        "    ##    ",
        " ######## ",
        "   ##  ## ",
        " ######## "
    ]
    
    for line in pattern_lines:
        print((line + "   ") * 5)


# --- 3. График функции y = sqrt(x) ---
def plot_sqrt_function():
    print("\n" + "-" * 30)
    print(f"## 📈 3. График функции $y = \\sqrt{{x}}$ (1-я четверть, высота $\\ge 9$ строк)")
    
    max_x = 81
    max_y_to_plot = 9 
    
    points = set()
    for x in range(max_x + 1):
        y = math.sqrt(x)
        if round(y) <= max_y_to_plot:
            points.add((x, round(y)))
    
    for current_y in range(max_y_to_plot, -1, -1):
        line = f"{current_y:2}|" 
        
        for current_x in range(max_x + 1):
            if (current_x, current_y) in points:
                line += "#"
            elif current_y == 0 and current_x != 0:
                 line += "-"
            else:
                line += " "

        print(line)
    
    x_labels = "   " + "".join([str(x)[-1] if x % 10 == 0 else " " for x in range(max_x + 1)])
    print(x_labels)


# --- 4. Диаграмма сравнения средних по модулю ---
def analyze_and_plot_averages():
    print("\n" + "-" * 30)
    print("## 📊 4. Диаграмма сравнения среднего по модулю")
    
    numbers = get_sequence_data()
    total_count = len(numbers)
    
    if total_count < 250:
        print(f"Внимание: Найдено только {total_count} чисел. Сравнение будет выполнено для двух половин ({total_count//2}/{total_count - total_count//2}).")
        split_index = total_count // 2
    else:
        split_index = 125

    group1 = numbers[:split_index]
    group2 = numbers[split_index:split_index*2]

    avg_abs1 = sum(abs(n) for n in group1) / len(group1) if len(group1) > 0 else 0
    avg_abs2 = sum(abs(n) for n in group2) / len(group2) if len(group2) > 0 else 0
    
    max_avg = max(avg_abs1, avg_abs2, 1)
    
    BAR_COLOR1 = '\033[46m'
    BAR_COLOR2 = '\033[45m'
    RESET = '\033[0m'
    max_bar_length = 50
    
    bar_length1 = int((avg_abs1 / max_avg) * max_bar_length)
    bar_length2 = int((avg_abs2 / max_avg) * max_bar_length)

    print(f"Первая группа ({len(group1)} чисел): Среднее по модулю: {avg_abs1:.2f}")
    print(f"Вторая группа ({len(group2)} чисел): Среднее по модулю: {avg_abs2:.2f}")
    
    bar1 = f"{BAR_COLOR1}{' ' * bar_length1}{RESET}"
    print(f"Группа 1: {bar1}")
    
    bar2 = f"{BAR_COLOR2}{' ' * bar_length2}{RESET}"
    print(f"Группа 2: {bar2}")


# --- 5. Допзадание: Анимация ---
def clear_console():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        print("\n" * 50) 

def simple_animation(frames=2, repetitions=5):
    print("\n" + "-" * 30)
    print("## 🎬 Допзадание: Анимация")
    print("Анимация запустится через 2 секунды. Нажмите Ctrl+C для остановки.")
    time.sleep(2)
    
    frame1 = "\n" * 3 + "        (o.o)" 
    frame2 = "\n" * 4 + "        (O_O)"
    animation_frames = [frame1, frame2]
    
    try:
        for _ in range(repetitions):
            for i in range(frames):
                clear_console()
                print("--- Анимация ---")
                print(animation_frames[i % len(animation_frames)])
                time.sleep(0.3)
    except KeyboardInterrupt:
        pass
    
    clear_console()
    print("Анимация завершена!")


if __name__ == "__main__":
    draw_polish_flag()
    draw_d_pattern()
    plot_sqrt_function()
    analyze_and_plot_averages()
    
    # Раскомментируйте для анимации
    # simple_animation()
    print("\n" + "-" * 30)
    print("Чтобы увидеть анимацию, раскомментируйте вызов 'simple_animation()' и запустите код в консоли.")