import { useCallback, useState, useEffect } from "react";
import "./checktraffic.css";
import axios from 'axios';
import { io } from 'socket.io-client';


function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
  
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    const size = bytes / Math.pow(k, i);
  
    return `${size.toFixed(2)} ${sizes[i]}`;
  }
function Checktraffic() {
  const [file, setFile] = useState(null);
  const [size, setSize] = useState(null);
  const [preview, setPreview] = useState(null);
  const [frameCount,setFrameCount] = useState(null);
  const [totalFrame,settotalFrame] = useState(null);
  
  useEffect(() => {
    const socket = io('http://localhost:5000');
    socket.on('frameCount', (data) => {
        setFrameCount(prev=>data);
    });
    socket.on('totalFrames', (data) => {
        settotalFrame(prev=>data);
    });

    // Send message to server
    socket.emit('client_message', { msg: 'Hello from React!' });

    // return () =>{alert("disconnected"); socket.disconnect()};
  }, []);

  const uploadFile = async (file) => {
    const formData = new FormData();
    formData.append('file', file);
    try {
      const res = await axios.post('http://localhost:5000/video', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      document.querySelector(".analyze").style.display = "none"
      document.querySelector(".uploading").style.display = "none"
      document.querySelector(".result").style.display = "block"
      document.querySelector(".result video").setAttribute("src",res.data["Status"])
      console.log(res.data)
    } catch (err) {
      console.error('Upload error:', err);
    }
  };
  const handleDrop = useCallback((e) => {
    e.preventDefault();
    const droppedFile = e.dataTransfer.files[0];
    if (droppedFile) {
      setSize(prev=>droppedFile.size);
      setFile(droppedFile);
      setPreview(URL.createObjectURL(droppedFile));
      uploadFile(droppedFile);
    }
  }, []);

  const handleDragOver = (e) => {
    e.preventDefault(); // necessary to allow drop
  };

  return (
    <div className="traffic">
      <h2>Get Traffic Details Here!</h2>
      <h4>Get Vehicle Count, Vehicle Type, Vehicle number. All in one Place</h4>

      <div
        className="drag"
        onDrop={handleDrop}
        onDragOver={handleDragOver}
        style={{
          border: "2px dashed #999",
          borderRadius: "8px",
          padding: "40px",
          textAlign: "center",
          color: "#555",
        //   height: file ? "max-content" : null,
        }}
      > 
        {file ? (
          <div className="uploading">
            <h1><i class='bx bx-file' ></i> File: {file.name}</h1>
            {/* {file.type.startsWith('image/') && (
            <img src={preview} alt="preview" style={{ maxWidth: '100%', marginTop: 20 }} />
          )} */}
            <video src={preview} controls></video>
            <aside>
                <h3><i class='bx bx-sushi'></i> Size : {formatFileSize(size)}</h3>
                <h3><i class='bx bx-ghost'></i> Type : {file.type}</h3>
                <h3><i class='bx bx-calendar' ></i> Last Modified Date : {Date(file.lastModified).split("GMT")[0].split("2025")[0]}</h3>
                <h3><i class='bx bx-time'></i> LastModifiedTime : {Date(file.lastModified).split("GMT")[0].split("2025")[1]}</h3>
                <div><p>Added 1 File</p><button onClick={()=>{document.querySelector(".analyze").style.display = "block";document.querySelector(".uploading").style.display = "none"}}>Start Analyzing <i class='bx bx-objects-vertical-bottom' ></i></button></div>
            </aside>
          </div>
        ) : (
          <p>Drag & drop a file here</p>
        )}

      <div className="analyze">
        <img src="/analyze.gif" alt="" />
        <h5>Anallyzing Frames <span>{frameCount} / {totalFrame}</span></h5>
        <h6>Please Wait...</h6>
      </div>
      <div className="result">
        <video src={null} muted controls autoPlay></video>
      </div>
      </div>
    </div>
  );
}

export default Checktraffic;



