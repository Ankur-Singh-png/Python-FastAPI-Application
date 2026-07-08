import { useEffect, useState } from "react";
import api from "../api/api";

function Folders() {

    const [folders, setFolders] = useState([]);

    const [name, setName] = useState("");
    const [ownerId, setOwnerId] = useState("");

    useEffect(() => {
        getFolders();
    }, []);

    async function getFolders() {
        try {
            const response = await api.get("/folders");
            setFolders(response.data);
        } catch (error) {
            console.error(error);
        }
    }

    async function createFolder() {
        try {

            await api.post("/folders", null, {
                params: {
                    name: name,
                    owner_id: ownerId
                }
            });

            setName("");
            setOwnerId("");

            getFolders();

        } catch (error) {
            console.error(error);
        }
    }

    async function deleteFolder(id) {

        try {

            await api.delete(`/folders/${id}`);

            getFolders();

        } catch (error) {
            console.error(error);
        }

    }

    return (

        <div className="page">

            <h2>Folder Management</h2>

            <input
                type="text"
                placeholder="Folder Name"
                value={name}
                onChange={(e) => setName(e.target.value)}
            />

            <input
                type="number"
                placeholder="Owner ID"
                value={ownerId}
                onChange={(e) => setOwnerId(e.target.value)}
            />

            <button onClick={createFolder}>
                Create Folder
            </button>

            <hr />

            <table>

                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Folder Name</th>
                        <th>Owner ID</th>
                        <th>Action</th>
                    </tr>
                </thead>

                <tbody>

                    {
                        folders.map(folder => (

                            <tr key={folder.id}>

                                <td>{folder.id}</td>
                                <td>{folder.name}</td>
                                <td>{folder.owner_id}</td>

                                <td>

                                    <button
                                        onClick={() => deleteFolder(folder.id)}
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

export default Folders;