describe('template spec', () => {
  it('passes', () => {
    cy.visit('http://localhost:5000/');
    cy.get('button').click();
    cy.contains('body', 'Click');
    // other syntax
    // cy.get('body').should(($p) => {
    //     expect($p).to.contain('Click')
    // });
  })
})