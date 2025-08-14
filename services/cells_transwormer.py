def cell_to_coordinates(cell):
    """
    Переводит шахматную нотацию клетки в координаты (x, y, z).
    
    Args:
        cell (str): Клетка в формате "A1", "B2", etc.
    
    Returns:
        tuple: (x, y, z) координаты клетки
    
    Raises:
        ValueError: Если формат клетки неверный
    """
    if len(cell) != 2:
        raise ValueError("Клетка должна быть в формате 'A1', 'B2', etc.")
    
    # Извлекаем столбец (букву) и строку (цифру)
    col_letter = cell[0].upper()
    row_number = cell[1]
    
    # Проверяем корректность входных данных
    if col_letter not in 'ABCDEFGH':
        raise ValueError("Столбец должен быть от A до H")
    
    if row_number not in '12345678':
        raise ValueError("Строка должна быть от 1 до 8")
    
    # Преобразуем в индексы (0-7)
    col_index = ord(col_letter) - ord('A')  # A=0, B=1, ..., H=7
    row_index = int(row_number) - 1         # 1=0, 2=1, ..., 8=7
    
    # Базовые координаты для клетки A1 (левый нижний угол)
    base_x = -1.525
    base_y = -1.525
    base_z = 0.0
    
    # Шаг между клетками
    step = 0.436  # Примерно (1.525 - (-1.525)) / 7 ≈ 0.436
    
    # Вычисляем координаты
    x = base_x + col_index * step
    y = base_y + row_index * step
    z = base_z
    
    return (round(x, 3), round(y, 3), round(z, 3))


def coordinates_to_cell(x, y, z=0):
    """
    Переводит координаты в шахматную нотацию клетки.
    
    Args:
        x, y, z (float): Координаты точки
    
    Returns:
        str: Клетка в формате "A1", "B2", etc.
    """
    # Базовые координаты для клетки A1
    base_x = -1.525
    base_y = -1.525
    
    # Шаг между клетками
    step = 0.436
    
    # Вычисляем индексы
    col_index = round((x - base_x) / step)
    row_index = round((y - base_y) / step)
    
    # Проверяем границы
    if not (0 <= col_index <= 7) or not (0 <= row_index <= 7):
        raise ValueError("Координаты выходят за границы доски")
    
    # Преобразуем в шахматную нотацию
    col_letter = chr(ord('A') + col_index)
    row_number = str(row_index + 1)
    
    return col_letter + row_number


# Примеры использования:
if __name__ == "__main__":
    # Тестируем функции
    test_cells = ["A1", "A8", "H1", "H8", "D4", "E5"]
    
    print("Клетка -> Координаты:")
    for cell in test_cells:
        coords = cell_to_coordinates(cell)
        print(f"{cell:2} -> {coords}")
    
    print("\nОбратный перевод:")
    for cell in test_cells:
        coords = cell_to_coordinates(cell)
        back_cell = coordinates_to_cell(*coords)
        print(f"{coords} -> {back_cell}")
    
    # Проверим несколько координат из ваших данных
    print("\nПроверка с вашими данными:")
    # ID 97: (-1.525, -1.525) должно быть A1
    print(f"(-1.525, -1.525) -> {coordinates_to_cell(-1.525, -1.525)}")
    # ID 128: (1.525, 1.525) должно быть H8  
    print(f"(1.525, 1.525) -> {coordinates_to_cell(1.525, 1.525)}")