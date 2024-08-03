import { useCallback } from "react"
import { useDropzone } from "react-dropzone"

interface ImageUploadProps {
 onUpload : (data:any)=>void
}

const ImageUpload:React.FC<ImageUploadProps> = ({onUpload}) => {
    const onDrop = useCallback((acceptedFiles:File[]) => {
        const image = acceptedFiles[0]
        let reader = new FileReader();

        reader.onloadend = function() {
            onUpload(reader.result)
        }
        reader.readAsDataURL(image);
    },[])

    const {getRootProps, getInputProps} = useDropzone({onDrop})

  return (
    <div className="border w-4/6 mx-auto h-auto p-3 rounded-sm flex items-center justify-center" {...getRootProps()}>
        <input {...getInputProps()} required />
            <div className="rounded-full bg-slate-100 p-2 aspect-square flex items-center justify-center border " >
                Upload Image
            </div>            
    </div>
  )
}

export default ImageUpload