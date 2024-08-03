
const Description = () => {
  return (
    <div className="space-y-6 flex-1">
        <div>
            <h1 className="text-xl text-center font-semibold">Project Overview</h1>
            <p>This project focuses on developing a machine learning model to classify images of 90 distinct animal classes using transfer learning techniques. The aim was to leverage pre-trained models to improve the accuracy and efficiency of the classification task while handling a large and diverse dataset.</p>
        </div>
        <div>
            <h2 className="font-semibold text-xl mb-2 text-center">Technologies Used</h2>
            <div>
                <span className="font-semibold">Machine Learning Framework:</span> Tensorflow
            </div>
            <div><span className="font-semibold">Programming Language: </span> Python</div>
            <div><span className="font-semibold">Development Environment:</span> Google Colab</div>
            <div><span className="font-semibold">Pre-trained Model:</span> MobileNet</div>
        </div>
        <div className="space-y-2">
            <h1 className="font-semibold text-xl mb-2 text-center">Key Features</h1>
            <div><span className="font-semibold">Data Processing:</span> Employed various data augmentation techniques to enhance the training dataset, including rotation, scaling, and flipping of images.</div>
            <div>
                <span className="font-semibold">Model Selection:</span>
                Utilized several pre-trained models to identify the one that offers the best performance for this specific classification task.
            </div>
            <div>
                <span className="font-semibold">Transfer Learning:</span>
                Fine-tuned the selected pre-trained model on the dataset of 90 animal classes to leverage existing knowledge and improve classification accuracy.
            </div>
            <div>
                <span className="font-semibold">Evaluation Metrics:</span>
                Used accuracy, precision, recall, and F1-score to evaluate model performance, ensuring a robust and reliable classifier.
            </div>
        </div>
    </div>
  )
}

export default Description