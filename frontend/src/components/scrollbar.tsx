import { ScrollArea } from "./ui/scroll-area"

interface ScrollbarProps {
    items : string[]
}

const Scrollbar:React.FC<ScrollbarProps> = ({items}) => {
  return (
    <ScrollArea className="sm:w-1/5 w-[52] h-[600px] rounded-md border">
        <div className="p-2">
            <h4 className="mb-4 font-medium leading-none">Animal Tags</h4>
            {
                items.map(item=>(
                <>
                    <div key={item}>
                    <a target="_blank" href={`https://www.google.com/search?tbm=isch&q=${item}`} className="text-sm" key={item}>
                        {item.slice(0,1).toUpperCase() + item.slice(1)}
                    </a>
                    </div>
                </>))
            }
        </div>
    </ScrollArea>
  )
}

export default Scrollbar