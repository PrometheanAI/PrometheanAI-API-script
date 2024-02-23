# PrometheanAI API script
Write custom scripts to keep Promethean library synced to your automated workflows or
integrate Promethean functionality directly inside of your tools with just a few lines of code

SEARCH ASSETS IN LIBRARY FUNCTION
<br>Description:
<br>This function allows searching within the Promethean Libraries, enabling users to locate specific assets efficiently.

<br>It accepts two parameters:

<br>'search term' - A string representing the item or concept the user desires to find within the libraries.
<br>'asset_type' -  Denotes the category or type of assets to search within. Users can specify the mode of search based on their requirements, including custom modes.

<br>The 'asset_type' argument is responsible for the mode in which you want to search.
<br>Currently, you can search in every mode that you have, even if it's your custom mode.

<br>NOTE: Before executing this function, ensure the Promethean Browser or Command Line interface is operational.
<br>The function's execution retrieves assets matching the specified search_term and asset_type.

<br>Example:
<br>from promethean_ai_api import search_assets_in_library, AssetTypes
<br>result = search_assets_in_library('leather couch', AssetTypes.SOURCE_FILE)


ADD FILES TO LIBRARY SCRIPT
This function allows you to add files to the Promethean Browser.
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

<br>Example:
<br>from promethean_ai_api import search_assets_in_library, AssetTypes
<br>result = search_assets_in_library('leather couch', AssetTypes.SOURCE_FILE)
