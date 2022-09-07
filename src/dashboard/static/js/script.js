















const url = window.location.href
const searchInput = document.getElementById('search-input')
const searchForm = document.getElementById('search-form')
const resultsBox = document.getElementById('results-box')

// const results_card = document.getElementsByClassName('.results-card')

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value


const sendSearchData = (structures) => {
  $.ajax({
    type: 'POST',
    url: 'search/',
    data: {
      'csrfmiddlewaretoken': csrf,
      'structures': structures,
    },
    success: (res)=> {
      console.log(res)
    },
    error: (err) =>{
      console.log(err)
    }
  })
}

searchInput.addEventListener('keyup', e=>{
  console.log(e.target.value)

  if (resultsBox.classList.contains('not-visible')){
    resultsBox.classList.remove('not-visible')
  }
  sendSearchData(e.target.value)
})