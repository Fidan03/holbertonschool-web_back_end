import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(req, res) {
    const databasePath = process.argv[2];

    readDatabase(databasePath)
      .then((fields) => {
        let output = 'This is the list of our students';

        Object.keys(fields)
          .sort((a, b) => a.localeCompare(b, 'en', { sensitivity: 'base' }))
          .forEach((field) => {
            const names = fields[field];
            output += `\nNumber of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
          });

        res.status(200).send(output);
      })
      .catch((err) => {
        res.status(500).send(err.message);
      });
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    const databasePath = process.argv[2];

    readDatabase(databasePath)
      .then((fields) => {
        const names = fields[major] || [];
        res.status(200).send(`List: ${names.join(', ')}`);
      })
      .catch((err) => {
        res.status(500).send(err.message);
      });
  }
}

export default StudentsController;
