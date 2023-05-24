from PIL import Image

# Assuming the original image is located in the "static" folder
original_image_path = '/Users/abcbrianlee/CS Folder/ECommerce_Site/website/static/versace5.jpg'

# Define the desired width and height for the resized image
desired_width = 320
desired_height = 320

# Open the original image
original_image = Image.open(original_image_path)

# Resize the image
resized_image = original_image.resize((desired_width, desired_height))

# Save the resized image to a new file
resized_image_path = '/Users/abcbrianlee/CS Folder/ECommerce_Site/website/static/versace_resize5.jpg'
resized_image.save(resized_image_path)
