let items = document.querySelectorAll('.questions-box .questions-list')
let activeItemIndex = -1
Array.prototype.forEach.call(items, function(item, index) {
  const currentLink = item.querySelector('.questions-article')
  const currentAnswer = item.querySelector('.questions-answer')
  currentLink.addEventListener('click', function(){
    if (activeItemIndex !== -1 && activeItemIndex !== index) {
      items[activeItemIndex].querySelector('.questions-article').classList.remove('questions-article-active')
      items[activeItemIndex].querySelector('.questions-answer').classList.remove('questions-answer-active')
    }
    if (activeItemIndex !== index) {
      currentLink.classList.add('questions-article-active')
      currentAnswer.classList.add('questions-answer-active')
      activeItemIndex = index
    }
    else {
      currentLink.classList.remove('questions-article-active')
      currentAnswer.classList.remove('questions-answer-active')
      activeItemIndex = -1
    }
  })
})

/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {

    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}