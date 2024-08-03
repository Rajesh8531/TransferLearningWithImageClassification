interface HeaderProps {
    title : string
}

const Header:React.FC<HeaderProps> = ({title}) => {
  return (
    <div className="w-full text-3xl lg:text-4xl font-semibold text-center">
        {title}
    </div>
  )
}

export default Header