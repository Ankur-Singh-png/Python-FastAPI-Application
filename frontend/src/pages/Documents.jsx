import { useEffect, useState } from "react";
import api from "../api/api";

function Documents() {

    const [documents, setDocuments] = useState([]);

    const [title, setTitle] = useState("");
    const [filename, setFilename] = useState("");
    const [folderId, setFolderId] = useState("");
    const [uploadedBy, setUploadedBy] = useState("");

    useEffect(() => {
        getDocuments();
    }, []);

    async function getDocuments() {

        try {

            const response = await api.get("/documents");

            setDocuments(response.data);

        } catch (error) {

            console.log(error);

        }

    }

    async function createDocument() {

        try {

            await api.post("/documents", null, {

                params: {

                    title: title,
                    filename: filename,
                    folder_id: folderId,
                    uploaded_by: uploadedBy

                }

            });

            setTitle("");
            setFilename("");
            setFolderId("");
            setUploadedBy("");

            getDocuments();

        } catch (error) {

            console.log(error);

        }

    }

    async function deleteDocument(id) {

        try {

            await api.delete(`/documents/${id}`);

            getDocuments();

        } catch (error) {

            console.log(error);

        }

    }

    return (

        <div className="page">

            <h2>Document Management</h2>

            <input
                type="text"
                placeholder="Document Title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
            />

            <input
                type="text"
                placeholder="File Name"
                value={filename}
                onChange={(e) => setFilename(e.target.value)}
            />

            <input
                type="number"
                placeholder="Folder ID"
                value={folderId}
                onChange={(e) => setFolderId(e.target.value)}
            />

            <input
                type="number"
                placeholder="Uploaded By (User ID)"
                value={uploadedBy}
                onChange={(e) => setUploadedBy(e.target.value)}
            />

            <button onClick={createDocument}>
                Create Document
            </button>

            <hr />

            <table>

                <thead>

                    <tr>

                        <th>ID</th>
                        <th>Title</th>
                        <th>Filename</th>
                        <th>Folder ID</th>
                        <th>Uploaded By</th>
                        <th>Action</th>

                    </tr>

                </thead>

                <tbody>

                    {

                        documents.map(document => (

                            <tr key={document.id}>

                                <td>{document.id}</td>
                                <td>{document.title}</td>
                                <td>{document.filename}</td>
                                <td>{document.folder_id}</td>
                                <td>{document.uploaded_by}</td>

                                <td>

                                    <button
                                        onClick={() => deleteDocument(document.id)}
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

export default Documents;