def get_price_or_rent(id, data):
    # Determine the default value based on whether 'price' or 'rent' is present
    default = data.get(
        'price') if 'price' in data else data.get('rent')

    # Loop through each comparable
    for comparable in data.get('comparables', []):
        # If the ID matches, return the price
        if comparable.get('id') == id:
            return comparable.get('price')

    # If no match is found in comparables, return the default
    return default
