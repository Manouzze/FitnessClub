
const edit_btn = document.getElementsByClassName(".edit-btn");
const input = document.getElementsByClassName(".input-franchise");

function editStructure(){
  edit_btn.addEventListener('click', function(){
    input.style.display="block";
  })
}

editStructure()