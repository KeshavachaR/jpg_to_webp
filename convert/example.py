
from jpg_to_webp_converter import jpg_to_webp

if __name__ == "__main__":
    jpg_url = ["https://t4.ftcdn.net/jpg/01/35/97/83/360_F_135978399_qplk3WPu7JOA63JPCYVy1fb7MI4nefAL.jpg",
               "https://t4.ftcdn.net/jpg/03/32/46/23/360_F_332462369_64Y5qJ7tLTS95Ycak2t8aWwEC6Hvleph.jpg"
               ]  
    output_file = "converted_jpg's"
    jpg_to_webp(jpg_url, output_file)
