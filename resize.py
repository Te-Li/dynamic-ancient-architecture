from PIL import Image, ImageSequence

def resize_gif(input_path, output_path, new_size=(400, 300)):

    with Image.open(input_path) as im:
        frames = [frame.copy() for frame in ImageSequence.Iterator(im)]
        
        resized_frames = [frame.resize(new_size, Image.LANCZOS) for frame in frames]
        
        resized_frames[0].save(output_path, save_all=True, append_images=resized_frames[1:], duration=im.info['duration'], loop=0)

input_path = 'combined.gif' 
output_path = 'resized.gif' 
resize_gif(input_path, output_path)
