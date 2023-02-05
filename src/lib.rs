use pyo3::prelude::*;
use xdot::parse;

#[pyfunction]
fn parse_to_py() {
    
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn gvrender(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(parse_to_py, m)?)?;

    Ok(())
}
