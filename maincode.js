const { ml5 } = window; // recalled the ml5 library
const classifier = ml5.imageClassifier("https://teachablemachine.withgoogle.com/models/eWLyrlvSW/model.json", console.log);// recalls google teachablemachine link and code
//created a new imageClassifier using the previous function.


const result = document.querySelector(".result h2");
const image = document.querySelector(".image");
//these functions allow us to use the HTMLelement with the class of image in our index file
  const results = await classifier.classify(image);
  result.innerText = results[0].label;
}// classfies image and labels to most probabable result

function handleUpload(files) {
  image.src = URL.createObjectURL(files[0]);
  setTimeout(classifyImage, 50);
}// allows to upload or take picture of file
