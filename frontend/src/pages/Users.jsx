import { useEffect, useState } from "react";
import api from "../api/api";

function Users() {

    const [users, setUsers] = useState([]);

    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    useEffect(() => {
        getUsers();
    }, []);

    async function getUsers() {
        try {
            const response = await api.get("/users");
            setUsers(response.data);
        } catch (error) {
            console.log(error);
        }
    }

    async function createUser() {

        try {

            await api.post("/users", null, {
                params: {
                    username,
                    email,
                    password
                }
            });

            setUsername("");
            setEmail("");
            setPassword("");

            getUsers();

        } catch (error) {
            console.log(error);
        }

    }

    async function deleteUser(id) {

        try {

            await api.delete(`/users/${id}`);

            getUsers();

        } catch (error) {
            console.log(error);
        }

    }

    return (

        <div className="page">

            <h2>Users</h2>

            <input
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
            />

            <input
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />

            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />

            <button onClick={createUser}>
                Create User
            </button>

            <hr />

            <table>

                <thead>

                    <tr>

                        <th>ID</th>
                        <th>Username</th>
                        <th>Email</th>
                        <th>Action</th>

                    </tr>

                </thead>

                <tbody>

                    {
                        users.map(user => (

                            <tr key={user.id}>

                                <td>{user.id}</td>
                                <td>{user.username}</td>
                                <td>{user.email}</td>

                                <td>

                                    <button
                                        onClick={() => deleteUser(user.id)}
                                    >
                                        Delete
                                    </button>

                                </td>

                            </tr>

                        ))
                    }

                </tbody>

            </table>

        </div>

    );

}

export default Users;