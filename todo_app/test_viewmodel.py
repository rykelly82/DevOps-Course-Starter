from todo_app.data.item import Item
from todo_app.data.view_model import ViewModel


def test_done_items_property_only_shows_done_items_and_nothing_else():
    #Arrange
    items = [
        Item(1, "Started Todo", "To Do"),
        Item(2, "In Progress Todo", "Doing"),
        Item(3, "Finished Todo", "Done")
    ]
    view_model = ViewModel(items)
    

    #Act
    returned_items = view_model.done_items
    
    
    #Assert
    assert len(returned_items) == 1
    returned_single_item = returned_items [0]
    assert returned_single_item.status == "Done" 
