from rembg import remove
from PIL import Image
import io
import os

def remove_background():
    print("=== Убрать фон с изображения ===")
    
    # Get input file path from user
    while True:
        input_path = input("Введите путь к файлу: ").strip('"').strip()  # Remove any quotes and whitespace
        
        # Check if file exists
        if not os.path.exists(input_path):
            print(f"\nФайл не найден: {input_path}")
            print("Пожалуйста введите корректный путь.\n")
            continue
        
        # Check if it's an image file
        valid_extensions = ['.jpg', '.jpeg', '.png', '.webp']
        if not any(input_path.lower().endswith(ext) for ext in valid_extensions):
            print("\nПожалуйста предоставьте картинку формата .jpg, .png, .webp")
            continue
            
        break
    
    # Create output path
    base_path = os.path.splitext(input_path)[0]
    output_path = f"{base_path}_nobg.png"
    
    print("\nОбработка изображения...")
    
    # Process the image
    try:
        with open(input_path, 'rb') as input_file:
            input_image = input_file.read()
        
        output_image = remove(input_image)
        
        with open(output_path, 'wb') as output_file:
            output_file.write(output_image)
            
        print(f"Успешно! Итоговая картинка сохранена в: {output_path}")
        
        # Display the image if possible
        try:
            image = Image.open(io.BytesIO(output_image))
            image.show()
        except Exception as e:
            print(f"(Не удалось отобразить изображение: {str(e)})")
            
    except Exception as e:
        print(f"\nОшибка отображения изображения: {str(e)}")

if __name__ == "__main__":
    # Install required packages if not available
    try:
        from rembg import remove
    except ImportError:
        print("Отсутствуют необходимые пакеты. Установка rembg и onnxruntime....")
        import subprocess
        subprocess.run(['pip', 'install', 'rembg', 'onnxruntime', 'Pillow'], check=True)
        
    remove_background()
