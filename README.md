<h1>PrometheanAI API script</h1>
<p></p>Write custom scripts to keep Promethean library synced to your automated workflows or
integrate Promethean functionality directly inside of your tools with just a few lines of code</p>

<h2>SEARCH ASSETS IN LIBRARY FUNCTION</h2>
<p>Description:</p>
This function allows searching within the Promethean Libraries, enabling users to locate specific assets efficiently.

It accepts two parameters:

><p>'search term' - A string representing the item or concept the user desires to find within the libraries.</p>
><p>'asset_type' -  Denotes the category or type of assets to search within. Users can specify the mode of search based on their requirements, including custom modes.</p>

<p>The 'asset_type' argument is responsible for the mode in which you want to search.
Currently, you can search in every mode that you have, even if it's your custom mode.</p>

NOTE: Before executing this function, ensure the Promethean Browser or Command Line interface is operational.
The function's execution retrieves assets matching the specified search_term and asset_type.

Example:
```python
   from promethean_ai_api import search_assets_in_library, AssetTypes
   result = search_assets_in_library('leather couch', AssetTypes.SOURCE_FILE)
```


<h2>ADD FILES TO LIBRARY FUNCTION</h2>
<p>This function allows you to add files to the Promethean Browser.</p>
The function accepts files_data and three optional arguments: catalog_mode, silent_mode and force_overwrite.

The files_data argument can be passed in two ways:
   1. As a simple list of file paths if you want to let Promethean generate thumbnails.

   2. As a dictionary in the format {'path_to_file': {'thumbnail': 'path_to_thumbnail'}, ...}
      if you want to provide custom thumbnails.
      This option can be used for any file formats and useful if you already have archives with source files and
      Corresponding thumbnails to them.

The catalog_mode argument is responsible for the mode in which the files will be added in the browser.
      Currently, there are two modes available: Inspiration and Source Files.
      The Inspiration mode is designed for storing images only and useful for storing references, concept art and
      anything you want ot use as an inspiration for your project.
      The Source Files mode supports storing any kind of files and can be used as a library for your images, 3d files,
      and any kind of other files if you can provide custom thumbnails for them. In a way, Inspiration mode is a
      subset of Source Files mode.

The silent_mode argument suppresses any popup messages in the browser during the upload. This option is useful if you
     want to schedule the script to run regularly and don't want to interact with the browser. If this option is set to
     True, all the files that are already up-to-date in the library will be skipped. This will speed up the adding of
     new files to the library significantly in case you provide files from the same source folder every day.

The force_overwrite argument forces an update of all files from files_data, even if they already exist in the library.
     This option is useful if you want to update the custom thumbnails for the files that are already in the library.
     Please use this option only when you deliberately want to change the thumbnails for the files that are already in
     the library.

NOTE: Ensure that the Promethean Browser is open and running before executing the script.

Example ADD FILES TO LIBRARY: 1: <p>Add list of files to the library.</p>

```python
   import os
   from promethean_ai_api import add_files_to_library

   file_paths = [os.path.join(source_folder, file_name) for file_name in os.listdir(source_folder)]
   add_files_to_library(file_paths, asset_type=AssetTypes.INSPIRATION)
```

<br>Example ADD FILES TO LIBRARY: 2: <p>Add files with custom thumbnails to the library. Let's assume that we have archive with files and corresponding thumbnails in the same folder.</p>

```python
    import os
    from promethean_ai_api import add_files_to_library
    source_folder = r'C:\Test_folder'
    files_dict = {}
    archives_names = [file for file in os.listdir(source_folder) if file.endswith('.zip')]
    for archive_name in archives_names:
        file_path = os.path.join(source_folder, archive_name)
        thumbnail_path = os.path.join(source_folder, f'{os.path.splitext(archive_name)[0]}_thumbnail.jpg')
        if os.path.exists(thumbnail_path):
            files_dict[file_path] = {'thumbnail': thumbnail_path}
    
     add_files_to_library(files_dict)
```
