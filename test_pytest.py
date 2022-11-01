from main import documents, directories, get_all_doc_owners_names, show_document_info, add_new_doc, delete_doc
from ya_disk import upload, TOKEN

def test_get_all_doc_owners_names():
    result = get_all_doc_owners_names(documents)
    assert {'Аристарх Павлов', 'Геннадий Покемонов', 'Василий Гупкин'} == result


def test_show_document_info():
    result = show_document_info(documents)
    assert ['passport "2207 876234" "Василий Гупкин"', 
    'invoice "11-2" "Геннадий Покемонов"', 
    'insurance "10006" "Аристарх Павлов"'
    ] == result


def test_add_new_doc():
    add_ = 'g'
    result = add_new_doc(add_, add_, add_, add_)
    conclusion = documents , directories
    assert conclusion == result
    

def test_delete_doc():
    delete_ = "11-2"
    result = delete_doc(delete_)
    conclusion = documents , directories
    assert conclusion == result


def test_upload():
    result = upload('Music22', TOKEN)
    assert 201 == result