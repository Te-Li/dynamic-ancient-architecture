from PIL import Image, ImageSequence

def combine_gifs(gif_paths, output_path):

    with Image.open(gif_paths[0]) as im:
        frames = [frame.copy() for frame in ImageSequence.Iterator(im)]

    for path in gif_paths[1:]:
        with Image.open(path) as im:

            frames.extend([frame.copy() for frame in ImageSequence.Iterator(im)])

    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=im.info['duration'], loop=0)

gif_paths = ['2.gif', '4.gif','5.gif'] 
output_path = 'combined.gif' 
combine_gifs(gif_paths, output_path)
