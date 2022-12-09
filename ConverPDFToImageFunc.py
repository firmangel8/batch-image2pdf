from pdf2image import convert_from_path
import os


def flag_ok(value):
    return '\x1b[6;30;42m' + ' ' + value + ' ' + '\x1b[0m'


def check_extension(file, white_list_extension):
    if os.path.splitext(file)[1].lower() == "." + white_list_extension:
        return True
    else:
        return False


def console_info(info, status):
    flag = str(flag_ok(status))
    print(f'{info:<60s} {flag:<10s}')


def convert_pdf_inpage(path, path_url, result_path, prefix_page):
    images = convert_from_path(path)
    path_url_main_group = path_url + "_images"
    target_dir_out = os.path.basename(path).split('.')[0]
    new_dir = result_path + "/" + path_url_main_group + "/" + target_dir_out
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    for i in range(len(images)):
        target_path = new_dir + '/' + str(prefix_page) + str(i + 1) + '.jpg'
        images[i].save(target_path, 'JPEG')


def convertPDFBatch(path_url, result_path, prefix_page):
    for count, filename in enumerate(os.listdir(path_url)):
        link_path = path_url + '/' + filename
        if (check_extension(link_path, "pdf")):
            convert_pdf_inpage(link_path, path_url, result_path, prefix_page)
            console_info('Convert ' + link_path, "DONE")
    print('All exported done..')
