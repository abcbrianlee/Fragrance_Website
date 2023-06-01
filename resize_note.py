from PIL import Image
import sqlite3 

conn=sqlite3.connect('database.db')
cursor=conn.cursor()
cursor.execute('SELECT note_name from notes')
notes=cursor.fetchall()

desired_width = 175
desired_height = 175


for note in notes:
    note_name=note[0]

    original_image_path = f'/Users/abcbrianlee/CS Folder/ECommerce_Site/website/static/{note_name}note.jpg'

    resized_note_name = note_name.replace(' ', '_').lower()
    original_image = Image.open(original_image_path)
    resized_image = original_image.resize((desired_width, desired_height))
    resized_image_path = f'/Users/abcbrianlee/CS Folder/Ecommerce_Site/website/static/{note_name}_library.jpg'
    resized_image.save(resized_image_path)



cursor.close()
conn.close()