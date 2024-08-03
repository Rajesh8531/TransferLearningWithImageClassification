

const Layout = ({children}:{children:React.ReactNode}) => {

  return (
    <div className="w-full sm:w-4/5 lg:mx-auto space-y-6 h-full p-4 sm:p-6 lg:p-8">
        {children}
    </div>
  )
}

export default Layout