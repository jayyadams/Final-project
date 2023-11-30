import React, { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";

function AccountManager({ loggedInID, loggedIn, setLoggedIn }) {

    const [custData, setCustData] = useState({})
    const [makeChanges, setMakeChanges] = useState(true)
    const [showPassword, setShowPassword] = useState(false);
    const [newData, setNewData] = useState({
        name: "",
        username: "",
        password: "",
        email: ""
    });
    const history = useHistory()

    useEffect(() => {
        setNewData({
            name: custData.name,
            username: custData.user_name,
            password: custData.password,
            email: custData.email
        });
    }, [custData]);

    useEffect(() => {
        fetch(`customers/${loggedInID}`)
            .then((resp) => resp.json())
            .then(setCustData)
    }, [loggedInID])

    const updateInfo = async (e) => {
        e.preventDefault()
        try {
            const changedFields = {};

            // Compare each field in newData with custData and add changed ones to changedFields

            for (const key in newData) {
                if (newData[key] !== custData[key]) {
                    changedFields[key] = newData[key];
                }
            }
            const response = await fetch(`customers/${loggedInID}`, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(changedFields),
            });


            // // ReFetch Updated Data

            if (response.ok) {
                fetch(`customers/${loggedInID}`)
                    .then((resp) => resp.json())
                    .then(setCustData);

                setMakeChanges(true); // Switch back to view mode after updating
            } else {
                console.error('Failed to update customer information');
                alert('Failed to update customer information\n\n VALIDATION ERRORS');
            }
        } catch (error) {
            console.error('Error updating customer information', error);
        }
    };


    const handleChange = (e) => {
        const { name, value } = e.target
        setNewData({ ...newData, [name]: value })
    }
    const logOut = (e) => {
        setLoggedIn(!loggedIn)
        history.push('/')
    }

    // console.log(makeChanges)
    return (
        <div className="Changesform">{makeChanges ?
            <div className="ChangesDiv">
                <h1 className="NameChanges">Name:</h1>
                <p className="NameChangesinfo">{custData.name}</p>
                <br />
                <h1 className="EmailChanges">Email:</h1>
                <p className="EmailChangesinfo">{custData.email}</p>
                <br />
                <h1 className="UsernameChanges">UserName:</h1>
                <p className="UsernameChangesinfo">{custData.user_name}</p>
                <br />
                <h1 className="PassChanges">Password:</h1>
                <p className="PassChangesinfo">{custData.password}</p>
                <button className="MakeChanges" onClick={() => setMakeChanges(!makeChanges)}>Make Changes</button>
                <br/>
                <button className="LogoutChanges" onClick={logOut}>Logout</button>
            </div> :
            <div>
                <h2 className="EditAcc" align = 'center'>Edit Account</h2>
                <form id="regform" name="form" onSubmit={updateInfo}>
                    Name:<input
                        className="nameinput"
                        type="text"
                        name="name"
                        placeholder={custData.name}
                        value={newData.name}
                        onChange={handleChange}
                    />
                    <br />
                    Username:<input
                        className="usernameinput"
                        type="text"
                        name="username"
                        placeholder={custData.user_name}
                        value={newData.user_name}
                        onChange={handleChange} />
                    Password: <input
                        className="passwordinput"
                        type={showPassword ? "text" : "password"}
                        name="password"
                        placeholder={custData.password}
                        value={newData.password}
                        onChange={handleChange}
                    />
                    <button className="ShowPass" type='button' id="showPasswrd" onClick={() => setShowPassword(!showPassword)}>show password</button>
                    <br />
                    Email: <input
                        className="emailinput"
                        type="text"
                        name="email"
                        placeholder={custData.email}
                        value={newData.email}
                        onChange={handleChange} />
                    <br />
                    <input className="regbutt" id="register" type="submit" name="Register" ></input>
                    <br />
                    <button className="retbutt" type="button" onClick={() => setMakeChanges(!makeChanges)}>Return</button>
                </form>
            </div>}

        </div>
    )
}

export default AccountManager