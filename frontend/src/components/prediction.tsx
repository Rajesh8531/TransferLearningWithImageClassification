interface PredictionProps {
    imageData : string,
    prediction : string
}

const Prediction:React.FC<PredictionProps> = ({imageData,prediction}) => {
  return (
    <div className="flex-1 space-y-5">
        <img src={`${imageData}`} className="object-fill w-full h-96" />
        <div className="flex items-center ">
            <h2 className="text-xl text-center">Prediction : </h2>
            <p className="text-xl font-semibold"> &nbsp; {prediction}</p>
        </div>
    </div>
  )
}

export default Prediction