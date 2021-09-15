## analogy for scope - comparing it to the use of paper slips with the product id in argos -= the paper isnt taken into the store room, but the data off it is


def argosCounter(stockID):
    binloc = findTheGoods(stockID)
    goods = sendPicker(binloc)
    return goods

paper = argosCatSearch("saucepans with pyrex lid")

carBoot = argosCounter(paper)