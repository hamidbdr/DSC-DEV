import Login  from './../Login/Login.jsx';
import Logout from './../Logout/Logout.jsx';

function NavBar() {
    const logued = true

    return ( 
        <>
        <div>
            this the Nav Bar Element
            {logued ? <Login/> :  <Logout/>}
        </div>
        </>
     );
}

export default NavBar;