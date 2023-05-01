const loaderStyle = {
  width: "3rem",
  height: "3rem",
}

export default function Loading() {
  return <div className="spinner-border text-primary" role="status" style={loaderStyle} >
    <span className="visually-hidden">Loading...</span>
  </div>
}
