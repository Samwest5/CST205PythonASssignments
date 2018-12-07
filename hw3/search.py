# Sam Westigard
# Homework 3
# CST 205
# Contains search function,
# returns best match ID, Title, num tags matched


from imageInfo import info


def bestMatch(searchTags):


    # Initialize counts
    maxMatchesNum = 0
    maxMatchesTitle = info[0]['title']
    maxMatchesID = info[0]['id']
    found = False

    if len(searchTags) == 0:
        return 'noTag'

    # Check if any matches found
    for i in range(len(info)):

        imageTitleTags = info[i]['title'].split()
        imageTitleTags = set([x.lower() for x in imageTitleTags])
        imageOtherTags = info[i]['tags']
        imageOtherTags = set([x.lower() for x in imageOtherTags])
        imageTags = imageTitleTags | imageOtherTags

        for j in searchTags:

            if j in imageTags:
                found = True

    # If not matches return -1
    if not found:
        return 'noTag'

    # With at least one match search through combined tags of 'title' and 'tags'
    for i in range(len(info)):

        imageTitleTags = set(info[i]['title'].split())
        imageOtherTags = set(info[i]['tags'])
        imageTags = imageTitleTags | imageOtherTags
        imageTags = set([x.lower() for x in imageTags])


        # If found greater number of matches update new max
        if len(searchTags & imageTags) > maxMatchesNum:
            maxMatchesID = info[i]['id']
            maxMatchesTitle = info[i]['title']
            maxMatchesNum = len(searchTags & imageTags)
            matchedTags = searchTags & imageTags

        # If same matches found, determine which alphabetically first then update to new max
        if len(searchTags & imageTags) == maxMatchesNum:

            if maxMatchesTitle is not min(info[i]['title'], maxMatchesTitle):
                maxMatchesID = info[i]['id']
                maxMatchesTitle = info[i]['title']
                maxMatchesNum = len(searchTags & imageTags)
                matchedTags = searchTags & imageTags

    return maxMatchesID
