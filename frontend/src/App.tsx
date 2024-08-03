import { useState } from "react"
import Content from "./components/content"
import Header from "./components/header"
import ImageUpload from "./components/image-upload"
import Layout from "./components/layout"
import { Button } from "./components/ui/button"
import axios from "axios"


function App() {

  const [imageData,setImagedata] = useState<any>()
  const [isLoading,setIsLoading] = useState(false)
  const [prediction,setPrediction] = useState('')

  const onPredict = async ()=>{
    try {
      let cleanedBase64String = imageData.replace(/^data:image\/[a-zA-Z]+;base64,/, '');
      setIsLoading(true)
      const res = await axios.post('http://localhost:5000/predict',cleanedBase64String)
      setPrediction(res.data)
    } catch (error) {
      console.log(error)
    } finally {
      setIsLoading(false)
    }
  }


  return (
    <Layout>
      <Header title="Transfer Learning For Image Classification" />
      <div className="flex items-center">
        <ImageUpload onUpload={(data)=>setImagedata(data)} />
        <Button disabled={isLoading} onClick={onPredict} >Predict</Button>
      </div>
      <Content imageData={imageData} prediction={prediction} />
    </Layout>
  )
}

export default App
