import {useNavigate} from 'react-router-dom'

export const Home = () => {
    const navigate =useNavigate()

    return(
        <div >
            <h1> Dynamic Form</h1>
            <div className='mainbutton'>
            <button  onClick={() => navigate('create')}>Create New Form</button>
            <button onClick={() => navigate('existing')}>Open Existing Form</button>
            </div>
        </div>
    )
}