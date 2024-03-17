__author__ = ' Yigal Maksimov yigal.maksimov@prometheanai.com'
import json
import socket
import logging

LOCAL_TCP_IP = "127.0.0.1"
timeout_time = 180
max_msg_size = 2097152  # keep this chunk size

# TCP ports
BROWSER = 1312
CMD_LINE = 1313

class AssetTypes:
    INSPIRATION = 'inspiration'
    SOURCE_FILE = 'source_file'
    MESH = 'mesh'
    MATERIAL = 'material'
    TEXTURE = 'texture'
    # ....  You can add your custom modes here


def send_message_to_promethean(msg, target, with_reply=False):
    result_dict = None
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                # Connect to the server first to target that BROWSER_PORT in most cases
                client_socket.connect((LOCAL_TCP_IP, target))
            except ConnectionRefusedError:
                # If connection on BROWSER_PORT is refused, try connecting on CMD_LINE_PORT
                client_socket.connect((LOCAL_TCP_IP, CMD_LINE))
            # Set the timeout for receiving data
            client_socket.settimeout(timeout_time)
            # Prepare the message to be sent
            message = msg
            # Send the message
            client_socket.sendall(message.encode('utf-8'))
            if with_reply:
                # Shutdown the write operation
                client_socket.shutdown(socket.SHUT_WR)
                # Receive the reply from the server
                reply_chunk = client_socket.recv(max_msg_size).decode()
                # Parse the reply
                result_dict = json.loads(reply_chunk)
    except Exception as e:
        # Log the exception
        logging.exception(f"Couldn't send TCP message: {e}")
    finally:
        # Close the client socket
        client_socket.close()
    if with_reply:
        return result_dict


def search_assets_in_library(search_term, asset_type=AssetTypes.SOURCE_FILE):
# ======================================================================================================================
# +++ SEARCH ASSETS IN LIBRARY FUNCTION
# ======================================================================================================================
# Description:
# This function allows searching within the Promethean Libraries, enabling users to locate specific assets efficiently.

# It accepts two parameters:

# 'search term' - A string representing the item or concept the user desires to find within the libraries.
# 'asset_type' -  Denotes the category or type of assets to search within. Users can specify the mode of search based on their requirements, including custom modes.

# The 'asset_type' argument is responsible for the mode in which you want to search.
#      Currently, you can search in every mode that you have, even if it's your custom mode.
#
# NOTE: Before executing this function, ensure the Promethean Browser or Command Line interface is operational.
# The function's execution retrieves assets matching the specified search_term and asset_type.
# ======================================================================================================================

    result = send_message_to_promethean(
        msg=f'search_assets_in_library_by_keyword {json.dumps({"search_term": search_term, "asset_type": asset_type})}',
        target=BROWSER, with_reply=True)
    return result


def add_files_to_library(files_data, asset_type=AssetTypes.SOURCE_FILE, silent_mode=False, force_overwrite=False):
# ======================================================================================================================
# +++ ADD FILES TO LIBRARY FUNCTION
# ======================================================================================================================
# This function allows you to add files to the Promethean Browser.
# The function accepts files_data and three optional arguments: catalog_mode, silent_mode and force_overwrite.
#
# The files_data argument can be passed in two ways:
#   1. As a simple list of file paths if you want to let Promethean generate thumbnails.

#   2. As a dictionary in the format {'path_to_file': {'thumbnail': 'path_to_thumbnail'}, ...}
#      if you want to provide custom thumbnails.
#      This option can be used for any file formats and useful if you already have archives with source files and
#      Corresponding thumbnails to them.
#
# The catalog_mode argument is responsible for the mode in which the files will be added in the browser.
#      Currently, there are two modes available: Inspiration and Source Files.
#      The Inspiration mode is designed for storing images only and useful for storing references, concept art and
#      anything you want ot use as an inspiration for your project.
#      The Source Files mode supports storing any kind of files and can be used as a library for your images, 3d files,
#      and any kind of other files if you can provide custom thumbnails for them. In a way, Inspiration mode is a
#      subset of Source Files mode.
#
# The silent_mode argument suppresses any popup messages in the browser during the upload. This option is useful if you
#     want to schedule the script to run regularly and don't want to interact with the browser. If this option is set to
#     True, all the files that are already up-to-date in the library will be skipped. This will speed up the adding of
#     new files to the library significantly in case you provide files from the same source folder every day.
#
# The force_overwrite argument forces an update of all files from files_data, even if they already exist in the library.
#     This option is useful if you want to update the custom thumbnails for the files that are already in the library.
#     Please use this option only when you deliberately want to change the thumbnails for the files that are already in
#     the library.
#
# NOTE: Ensure that the Promethean Browser is open and running before executing the script.
# ======================================================================================================================

    send_message_to_promethean(
        msg=f'add_files_to_browser {json.dumps({"asset_type": asset_type, "files_data": files_data, "silent_mode": silent_mode, "force_overwrite": force_overwrite})}',
        target=BROWSER)


if __name__ == '__main__':
    import os
    source_folder = r'C:\Test_folder'

    # # Example SEARCH ASSETS IN LIBRARY: Search for assets by color 'red' in inspiration mode
    # search_assets_in_library(search_term='red', asset_type=AssetTypes.SOURCE_FILE)


    # # Example ADD FILES TO LIBRARY: 1: Add list of files to the library
    # file_paths = [os.path.join(source_folder, file_name) for file_name in os.listdir(source_folder)]
    # add_files_to_library(file_paths, asset_type=AssetTypes.INSPIRATION)


    # # Example ADD FILES TO LIBRARY: 2: Add files with custom thumbnails to the library. Let's assume that we have archive with files and
    # # corresponding thumbnails in the same folder.
    # files_dict = {}
    # archives_names = [file for file in os.listdir(source_folder) if file.endswith('.zip')]
    # for archive_name in archives_names:
    #     file_path = os.path.join(source_folder, archive_name)
    #     thumbnail_path = os.path.join(source_folder, f'{os.path.splitext(archive_name)[0]}_thumbnail.jpg')
    #     if os.path.exists(thumbnail_path):
    #         files_dict[file_path] = {'thumbnail': thumbnail_path}
    #
    # add_files_to_library(files_dict)
