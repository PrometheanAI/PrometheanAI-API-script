# PrometheanAI API script
Write custom scripts to keep Promethean library synced to your automated workflows or
integrate Promethean functionality directly inside of your tools with just a few lines of code

1.  SEARCH ASSETS IN LIBRARY FUNCTION
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
