function openRatingBox() {
    var modal = document.getElementById("modal");
    modal.style.display = "block";
  }
function openRatingBox2() {
    var modal2 = document.getElementById("modal2");
    modal2.style.display= "block";
}
  
  document.getElementById("ratingButton").addEventListener("click", openRatingBox);
  
  const commentInput = document.getElementById('commentInput');
  const charCount = document.getElementById('charCount');
  const maxChars = 200;
  
  commentInput.addEventListener('input', function() {
    const currentChars = this.value.length;
    charCount.textContent = currentChars + '/' + maxChars;
  
    if (currentChars > maxChars) {
      commentInput.classList.add('exceeded');
    } else {
      commentInput.classList.remove('exceeded');
    }
  });
  function closeModal(){
    var modal = document.getElementById("modal");
    modal.style.display ="none";
  }
  function closeModal2(){
    var modal2 = document.getElementById("modal2");
    modal2.style.display ="none";
  }

  document.querySelector(".close").addEventListener("click", function () {
    closeModal();
  });

  document.querySelector(".close2").addEventListener("click", function () {
    closeModal2();
  });
  function submitReview() {
    var comment = document.getElementById("commentInput").value;
    var product_id = document.getElementById("submitCommentButton").dataset.productId;
    var user_id = document.getElementById("submitCommentButton").dataset.userId;
    var rating = parseInt(document.getElementById("ratingValue").textContent);


  
    var data = {
      comment: comment,
      product_id: product_id,
      user_id: user_id,
      rating: rating

      
    };
  
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/product/store-comment", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
      if (xhr.readyState == 4 && xhr.status == 200) {
        console.log("Comment submitted Successfully");
        closeModal();
        openRatingBox2();
      }
    };
    xhr.send(JSON.stringify(data));

  }


  
document.getElementById("submitCommentButton").addEventListener("click", submitReview);
  
document.addEventListener("DOMContentLoaded", function() {
const stars= document.querySelectorAll('.star');

stars.forEach(star => {
  star.addEventListener('click', function(){
    const clickedValue = parseInt(this.getAttribute('data-value'));

    stars.forEach(star => {
      const starValue = parseInt(star.getAttribute('data-value'));
      star.src = (starValue <= clickedValue) ? '/static/star.png' : '/static/unstar.png';
    });

    const ratingValue=document.getElementById('ratingValue');
    ratingValue.textContent=clickedValue;
  });
});
});
  
  